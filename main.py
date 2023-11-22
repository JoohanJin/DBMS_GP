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
from tkinter import messagebox
from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import sqlite3
from PIL import Image, ImageTk
import smtplib
import webbrowser
from email.message import EmailMessage
import io

# GLOBAL VARIABLE
# DB connection 
db_connection = mysql.connector.connect(host="localhost", user="joe", passwd="1Q2w#E$R!!", database="project")
cursor = db_connection.cursor()
current_id = ""
recognized = 0

class HomePage:
    def __init__(self, id):
        global current_time
        global date_stamp
        global time_stamp

        # get the student id
        self.root = Tk()
        self.id = id

        query = "SELECT login_date, login_time, logout_date, logout_time FROM LogIn_Time WHERE student_id = %s"
        val = (id,)

        cursor.execute(query, val)
        result = cursor.fetchall()

        last_login_timestamp = result[0][1]
        last_login_datestamp = result[0][0]
        last_logout_datestamp = result[0][2]
        last_logout_timestamp = result[0][3]

        # print(f"last log in: {last_login_datestamp} {last_login_timestamp}\nlast log out: {last_logout_datestamp} {last_logout_timestamp}")

        current_time = time.time()
        self.date_stamp = datetime.datetime.fromtimestamp(current_time).strftime("%Y-%m-%d")
        self.time_stamp = datetime.datetime.fromtimestamp(current_time).strftime("%H:%M:%S")

        # login time and login date update
        update_time = "UPDATE LogIn_Time SET login_date = %s, login_time = %s WHERE student_id = %s"
        val = (self.date_stamp, self.time_stamp, id, )
        cursor.execute(update_time, val)
        db_connection.commit()

        query = "SELECT email, username FROM Student WHERE student_id = %s"
        val = (self.id,)
        
        cursor.execute(query, val)
        result = cursor.fetchall()

        self.student_email = result[0][0]
        self.student_name = result[0][1]

        self.welcome_message = f"Hello, {self.student_name}. Welcome to HKU Student Website!\nYour last login time is {last_login_datestamp} {last_login_timestamp}."
        cursor.execute(query, val)
        result = cursor.fetchall()
        
        query = "SELECT course_id FROM Student_takingcourses WHERE student_id = %s"
        val = (id,)
        cursor.execute(query, val)
        result = cursor.fetchone()
        course_codes_taking = result
        
        courses_to_take = course_codes_taking[0].strip('{}').split()
        current_datetime = datetime.datetime.fromtimestamp(current_time)
        day_info = current_datetime.strftime("%A")
        print(day_info)

        query = "SELECT course_id, course_start_time, class_day FROM Course WHERE course_id = %s"
        for course in courses_to_take:
            val = (course, )
            cursor.execute(query, val)
            result = cursor.fetchall()
            print(result)
            


        query = "SELECT time_table_image FROM TimeTable WHERE student_id = %s"
        val = (id,)
        cursor.execute(query, val)
        image_result = cursor.fetchone()

        if image_result:
            image_data = image_result[0]
            image_stream = io.BytesIO(image_data)
            timetable_image = Image.open(image_stream)
            self._image = ImageTk.PhotoImage(timetable_image)
        else:
            self._image = PhotoImage(file='assets/image/HomeBackground.gif')


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

        self._HeadLabel = Label(self.root, text='abc', width=150, height=100, bg='#3C6739').place(x=-5500, y=1000)
        self._background = PhotoImage(file='assets/image/Background.gif')


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
        self._profile_image = PhotoImage(file='assets/image/ProfileFi.png')
        self._profile_image_label = Label(self.root, image=self._profile_image, width=100, height=140, bg='#3C6739')
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

        self.root.protocol('WM_DELETE_WINDOW', self.on_close)
        self.root.mainloop()
    
    def send_email(self):        # Replace the email address / create App Password in Gmail for new email. 
        email = self.student_email #https://www.youtube.com/watch?v=hSnd8iYBiIg 

        subject = "Course Information"
        message = f"Course: {self.course_label['text']}\n" \
                f"Classroom Address: {self.address_label['text']}\n" \
                f"Teacher's Message: {self.message_label['text']}\n" \
                f"Zoom Link: {self.zoom_label['text']}\n" \
                f"Lecture Notes: {self.notes_label['text']}\n"


        msg = EmailMessage()
        msg.set_content(message)
        msg['Subject'] = subject
        msg['From'] = "1@gmail.com"  # Replace with your email address
        msg['To'] = "1@gmail.com"

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login("1@gmail.com", "1")  # Replace with your email / pw
            server.send_message(msg)

        # Clear email entry
        self.email_entry.delete(0, self.root.tk.END)

    def on_close(self):
        current_time = time.time()
        date_stamp = datetime.datetime.fromtimestamp(current_time).strftime("%Y-%m-%d")
        time_stamp = datetime.datetime.fromtimestamp(current_time).strftime("%H:%M:%S")

        time_update_query = "UPDATE LogIn_Time SET logout_date = %s, logout_time = %s WHERE student_id = %s"
        val = (date_stamp, time_stamp, self.id,)
        response=messagebox.askyesno('Exit', 'Are you sure you want to exit?')
        if response:
            cursor.execute(time_update_query, val)
            db_connection.commit()

            self.root.destroy()


class LogInPage:
    def __init__(self):
        self.root = Tk()
        self.root.title("Login Form")
        self.root.geometry("550x550")  # Set the size of the window

        # Load background image
        self.bg_image = ImageTk.PhotoImage(Image.open("assets/image/HKU.png"))
        self.bg_label = Label(self.root, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create labels
        self.username_image = ImageTk.PhotoImage(Image.open("assets/image/User.png"))
        self.label_username = Label(self.root, image=self.username_image, height=45, width=90, bg='gray')
        self.label_username.place(x=130, y=330, anchor=CENTER)

        self.password_image = ImageTk.PhotoImage(Image.open("assets/image/PW.png"))
        self.label_password = Label(self.root, image=self.password_image, height=45, width=90, bg='white')
        self.label_password.place(x=130, y=430, anchor=CENTER)

        # Create input fields
        self.entry_username = Entry(self.root, bg="white", relief=FLAT)
        self.entry_username.place(x=130, y=370, anchor=CENTER)


        self.entry_password = Entry(self.root, bg="white", show="*", relief=FLAT)
        self.entry_password.place(x=130, y=470, anchor=CENTER)

        # Create login button
        login_image = ImageTk.PhotoImage(Image.open("assets/image/login2.png"))
        login_button = Button(self.root, image=login_image, command=self.manual_login, height=40, width=90, bg='white')
        login_button.place(x=380, y=450, anchor=CENTER)

        # Load image for another button
        image = ImageTk.PhotoImage(Image.open("assets/image/loginface.png"))

        # Create button with image and circular border
        image_button = Button(self.root, command=self.auto_login, image=image, height=78, width=100, bg='white')
        image_button.place(x=380, y=350, anchor=CENTER)

        if recognized:
            self.root.destroy()
        elif not recognized:
            self.root.mainloop()

    def auto_login(self):
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
                # if event is None or event == 'Exit':
                #     break

            cap.release()
            cv2.destroyAllWindows()

        if (recognized): 
            # hmm close the window and open the webpage
            print("Successfully logged in")
            self.root.destroy()
            HomePage(current_id)
            # openHomePage(current_id)

            # initiate the homepage tk code

    def manual_login(self):
        global recognized
        username = self.entry_username.get()
        password = self.entry_password.get()

        global current_id
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
                messagebox.showerror("Login Error", "Incorrect Password")
                print("Wrong PW!")
            # start the homepage code with student id.
        else:
            # display the error message
            messagebox.showerror("Login Error", "You are not a student")
            print("You are not a student")
        if recognized:
            self.root.destroy()
            webapp = HomePage(current_id)

if __name__=="__main__":
    # Read events and values from the window
    login_app = LogInPage()
