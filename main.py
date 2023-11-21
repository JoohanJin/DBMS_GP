import os
import cv2
import mysql.connector
import PySimpleGUI as sg
import pickle
import datetime
import sys
import time
import sqlite3
import tkinter.ttk as ttk
from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import sqlite3
from PIL import Image, ImageTk

# GLOBAL VARIABLE
# DB connection 
db_connection = mysql.connector.connect(host="localhost", user="joe", passwd="1Q2w#E$R!!", database="project")
cursor = db_connection.cursor()
recognized = 0
current_id = ""

class HomePage:
    def __init__(self, id):
        # get the student id
        self.root = Tk()
        self.id = id
        

        self.root.geometry('1280x800')
        self.root.resizable(0, 0)
        self.root.title('Student Login')
        self.root.config(bg='white')

        global USERNAME
        global PASSWORD
        USERNAME = StringVar()
        PASSWORD = StringVar()

        head_img = Image.open('assets/image/HEADER5.png')
        head_img = ImageTk.PhotoImage(head_img)
        # self._Header = PhotoImage(file="./assets/image/HEADER5.png")
        self.HeaderLabel = Label(self.root, image=head_img, height=300, width=300)#.place(x=500, y=2000)
        self.HeaderLabel.place(x=500, y = 2000)

        self._Footer = PhotoImage(file="assets/image/FOOTER.png")

        self._HeadLabel = Label(self.root, text='abc', width=100, height=100, bg='#3C6739').place(x=-5500, y=1000)
        self._background = PhotoImage(file='assets/image/Background.gif')
        self._image = PhotoImage(file='assets/image/HomeBackground.gif')

        self._Label1 = Label(self.root, image=self._background).place(x=0, y=0)
        self._Label2 = Label(self.root, image=self._image).place(relx=0.5, rely=0.5, anchor='center', height=450, width=920)

        self._HeaderLabel = Label(self.root, image=head_img, text='Teacher', width=1277, height=80, bg='#3C6739').place(
            x=0, rely=0)
        self._FooterLabel = Label(self.root, image=self._Footer, height=40, width=1277, bg='#3C6739').place(x=0.5, y=677)

        # Load the dashboard image
        self._dashboard_image = PhotoImage(file='assets/image/Dashboard3.png')
        self._dashboard_label = Label(self.root, image=self._dashboard_image, height=588, width=190, bg='#3C6739')
        self._dashboard_label.place(x=0, y=85)

        # Create buttons for the dashboard
        self._profile_image = PhotoImage(file='assets/image/12.png')
        self._profile_image_label = Label(self.root, image=self._profile_image, width=100, height=100, bg='#3C6739')
        self._profile_image_label.place(x=40, y=100)
        
        self._Button1_image = PhotoImage(file='assets/image/Time.png')
        self._Button1_button = Button(self.root, image=self._Button1_image, width=170, height=50, bg='#3C6739')
        self._Button1_button.place(x=10, y=310)

        self._Button2_image = PhotoImage(file='assets/image/Discussion.png')
        self._Button2 = Button(self.root, image=self._Button2_image, width=160, height=40, bg='#3C6739')
        self._Button2.place(x=10, y=375)

        self._Button3_image = PhotoImage(file='assets/image/Zoom.png')
        self._Button3 = Button(self.root, image=self._Button3_image, width=150, height=40, bg='#3C6739')
        self._Button3.place(x=10, y=420)

        self._Button4_image = PhotoImage(file='assets/image/Lecture Notes.png')
        self._Button4 = Button(self.root, image=self._Button4_image, width=160, height=50, bg='#3C6739')
        self._Button4.place(x=10, y=250)


        self._Button5_image = PhotoImage(file='assets/image/Mater1.png')
        self._Button5 = Button(self.root, image=self._Button5_image, width=160, height=50, bg='#3C6739')
        self._Button5.place(x=3, y=470)

        self._Button6_image = PhotoImage(file='assets/image/Email.png')
        self._Button6 = Button(self.root, image=self._Button6_image, width=150, height=50, bg='#3C6739')
        self._Button6.place(x=10, y=520)

        self._Button7_image = PhotoImage(file='assets/image/log3.png')
        self._Button7 = Button(self.root, image=self._Button7_image, width=160, height=50, bg='#3C6739')
        self._Button7.place(x=10, y=620)

        self.root.mainloop()


def auto_login():
    global current_id
    global current_time
    global date_stamp
    global time_stamp
    global recognized
    gui_confidence = 60
    camera_time_period = 10
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
        # cv2.destroyAllWindows()

        if (recognized): 
            # hmm close the window and open the webpage
            print("Successfully logged in")
            # openHomePage(current_id)

            # initiate the homepage tk code

def manual_login(username, password):
    global current_id
    global recognized
    query = "SELECT pwd FROM Student WHERE student_id = %s"
    val = (username,)  # Convert username to a tuple
    cursor.execute(query, val)
    result = cursor.fetchall()

    if result:
        if result[0][0] == password:
            print("Successfully logged in")
            # openHomePage(username)
            recognized = 1
            current_id = username

        else:
            sg.popup("Wrong PIN")
            print("Wrong PW!")
        # start the homepage code with student id.
    else:
        # display the error message
        sg.popup("You are not a student!")
        print("You are not a student")

def register():
    return

if __name__=="__main__":
    # Define PySimpleGUI settings
    sg.theme('DarkAmber')

    # Define the layout of the GUI
    logo = sg.Image('src/HKU4.png', size=(300, 350))

    layout = [
        [sg.Column([[logo]], justification='center')],
        [sg.Text('Log In', size=(18, 1), font=('Any', 18),
                text_color='#FFFFFF', justification='center')],
        [sg.Button('😊', size=(5, 1), key='face_button'), sg.Button('EXIT')],
        [sg.Text('Student ID:'), sg.Input(key='username')],
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
    # recognized = 1
    while not recognized:
        event, values = window.Read()

        # Process the events
        if not event or event == 'EXIT':
            break

        # Get the values of the username and password inputs
        if event == "Log In":
            username = values['username']
            password = values['password']
            manual_login(username, password)
        
        if event == "face_button":
            auto_login()
    # window.close()
    

    app = HomePage(current_id)
    # app.mainloop()

    # Close the window