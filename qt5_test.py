import os
import cv2
import mysql.connector
import PySimpleGUI as sg
import pickle
from datetime import datetime
import login_page
import sys, res
from PyQt5 import QtCore, QtGui, QtWidgets
import PySimpleGUI as sg

if __name__=="__main__":
    gui_confidence = 60

    db_connection = mysql.connector.connect(host="localhost", user="joe", passwd="1Q2w#E$R!!", database="project")
    date = datetime.utcnow()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    cursor = db_connection.cursor()

    # Recognize and read
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("train.yml")

    labels = {"person_name": 1}
    with open("labels.pickle", "rb") as f:
        labels = pickle.load(f)
        labels = {v: k for k, v in labels.items()}

    face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    # Define PySimpleGUI settings
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = login_page.Ui_Form()
    ui.setupUi(Form)
    Form.show()

    # Process the events

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            # predict the id and confidence for faces
            id_, conf = recognizer.predict(roi_gray)

            # If the face is recognized
            if conf >= gui_confidence:
                font = cv2.QT_FONT_NORMAL
                id = 0
                id += 1
                name = labels[id_]
                current_name = name
                color = (255, 0, 0)
                stroke = 2
                cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), (2))

                # Find the student information in the database.
                select = "SELECT student_id, name, login_date, login_time, login_date FROM Student WHERE name='%s'" % (name)
                name = cursor.execute(select)
                result = cursor.fetchall()
                print(result)
                data = "error"

                for x in result:
                    data = x

                # If the student's information is not found in the database
                if data == "error":
                    # the student's data is not in the database
                    print("The student", current_name, "is NOT FOUND in the database.")

                # If the student's information is found in the database
                else:
                    """
                    Implement useful functions here.
                    Check the course and classroom for the student.
                        If the student has class room within one hour, the corresponding course materials
                            will be presented in the GUI.
                        if the student does not have class at the moment, the GUI presents a personal class 
                            timetable for the student.

                    """
                    update =  "UPDATE Student SET login_date=%s WHERE name=%s"
                    # update = "UPDATE test SET date_of_join=%s WHERE name=%s"
                    val = (date, current_name)
                    cursor.execute(update, val)
                    update = "UPDATE Student SET login_time=%s WHERE name=%s"
                    # update = "UPDATE test SET date_of_join=%s WHERE name=%s"
                    val = (current_time, current_name)
                    # cursor.execute(update, val)
                    db_connection.commit(update, val)

                    welcome_message = f""
                    # hello = ("Hello ", current_name, "You did attendance today")
                    # print(hello)
                    # engine.say(hello)


            # If the face is unrecognized
            else:
                color = (255, 0, 0)
                stroke = 2
                font = cv2.QT_FONT_NORMAL
                cv2.putText(frame, "UNKNOWN", (x, y), font, 1, color, stroke, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), (2))
                hello = ("Your face is not recognized")
                print(hello)
                # engine.say(hello)
                # engine.runAndWait()

        # GUI
        imgbytes = cv2.imencode('.png', frame)[1].tobytes() 
        if not win_started:
            win_started = True
            layout = [
                [sg.Text('Attendance System Interface', size=(30,1))],
                [sg.Image(data=imgbytes, key='_IMAGE_')],
            ]
            win = sg.Window('Attendance System',
                    default_element_size=(14, 1),
                    text_justification='right',
                    auto_size_text=False).Layout(layout).Finalize()
            image_elem = win.FindElement('_IMAGE_')
        else:
            image_elem.Update(data=imgbytes)

        event, values = win.Read(timeout=20)
        if event is None or event == 'Exit':
            break

    # Close the window
    sys.exit(app.exec_())
    