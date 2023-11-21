import os
import cv2
import mysql.connector
import PySimpleGUI as sg
import pickle
import datetime
import login_page
import sys
import PySimpleGUI as sg
import time

# GLOBAL VARIABLE
# DB connection 
db_connection = mysql.connector.connect(host="localhost", user="joe", passwd="1Q2w#E$R!!", database="project")
cursor = db_connection.cursor()
        

def auto_login(window):
    global current_time
    global date_stamp
    global time_stamp
    gui_confidence = 60
    camera_time_period = 10
    recognized = 0
    win_started = False

    current_time = time.time()
    camera_limit = current_time + camera_time_period

    date_stamp = datetime.datetime.fromtimestamp(current_time).strftime("%Y-%m-%d")
    time_stamp = datetime.datetime.fromtimestamp(current_time).strftime("%H:%M:%S")
    
    labels = {"person_name": 1}
    with open("labels.pickle", "rb") as f:
        labels = pickle.load(f)
        labels = {v: k for k, v in labels.items()}

    if time.time() < camera_limit:
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        try:
            recognizer.read("train.yml")
        except:
            error_msg = "Face Recognition Model has been corrupted or could not be found!"
            print(error_msg)
            # display msg?

        face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
        cap = cv2.VideoCapture(0)
        
        while True:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

            if recognized:
                break

            for (x, y, w, h) in faces:
                roi_gray = gray[y:y+h, x:x+ w]
                roi_color = frame[y:y+h, x:x+w]
                id_, conf = recognizer.predict(roi_gray)

                if conf >= gui_confidence:
                    font = cv2.QT_FONT_NORMAL
                    if id_ == 0:
                        id = "3035661360"
                    current_id = id
                    color = (255, 0, 0)
                    stroke = 2

                    # name = labels[id_]
                    # cv2.putText(frame, name,(x, y), font, 1, color, stroke, cv2.LINE_AA)

                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), (2))
                    recognized = 1
                    print("your face has been recognized")
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
            
            if time.time() > camera_limit:
                break

            # cv2.imshow('Checking your face id', frame)
            key_wait = cv2.waitKey(10) & 0xff
            if key_wait == 27:
                break

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

        cap.release()
        cv2.destroyAllWindows()

        if (recognized): 
            # hmm close the window and open the webpage
            window.close()
            print("Successfully logged in")

            # initiate the homepage tk code
            

    return

def show_notification(message):
    notification_layout = [
        [sg.Text(message)],
        [sg.Button('OK')]
    ]
    notification_window = sg.Window('Notification', notification_layout)

    while True:
        event, values = notification_window.read()
        if event == sg.WINDOW_CLOSED or event == 'OK':
            break

    notification_window.close()

def manual_login(username, password, window):
    query = "SELECT pwd FROM Student WHERE student_id = %s"
    val = (username,)  # Convert username to a tuple
    cursor.execute(query, val)
    result = cursor.fetchall()

    if result:
        if result[0][0] == password:
            window.close()
            print("Successfully logged in")
        else:
            sg.popup("Wrong PIN")
            print("Wrong PW!")
        # start the homepage code with student id.
    else:
        # display the error message
        sg.popup("You are not a student!", size=(300, 200))
        print("You are not a student")




def register():
    return




if __name__=="__main__":
    # Define PySimpleGUI settings
    sg.theme('DarkAmber')

    # Define the layout of the GUI
    # logo = sg.Image('assets/HKU4.png', size=(300, 350))

    layout = [
        # [sg.Column([[logo]], justification='center')],
        [sg.Text('Log In', size=(18, 1), font=('Any', 18),
                text_color='#FFFFFF', justification='center')],
        [sg.Button('😊', size=(5, 1), key='face_button'), sg.Button('EXIT')],
        [sg.Text('Username:'), sg.Input(key='username')],
        [sg.Text('Password:'), sg.Input(key='password', password_char='*')],
        [sg.Column([[sg.Button('Log In'), sg.Text('Forgot Password?')]], justification='center')],
    ]

    # Create the window
    window = sg.Window('ICMS Portal',
                    default_element_size=(30, 1),
                    element_justification='c',
                    text_justification='right',
                    auto_size_text=False).Layout(layout)

    # Read events and values from the window
    while True:
        event, values = window.Read()

        # Process the events
        if not event or event == 'EXIT':
            break

        # Get the values of the username and password inputs
        if event == "Log In":
            username = values['username']
            password = values['password']
            manual_login(username, password, window)
        
        if event == "face_button":
            auto_login(window)

    # Close the window
    window.Close()