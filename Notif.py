import tkinter as tk
from tkinter import *
import webbrowser
import smtplib
from email.message import EmailMessage

class CourseGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('500x570')
        self.resizable(0, 0)
        self.title('Notifications')
        self.config(bg='#333333')

        self._background = PhotoImage(file='/Users/zec/Desktop/Pic2/notiback3.png')
        self._Label1 = Label(self, image=self._background).place(x=0, y=0)

        # Create labels for course information
        label_font = ("Times New Roman", 14, "bold")  # Set the font for the labels

        self._course_label_image = tk.PhotoImage(file='/Users/zec/Desktop/Pic2/noticourse.png')
        self.course_label = tk.Label(self, image=self._course_label_image, width=150, height=40, bg='#3C6739')
        self.course_label.place(x=50, y=20, anchor=CENTER)

        self.text_label1 = Label(self, text='a' , font=('Times New Roman', 24), compound ='center')
        self.text_label1.place(x=100, y=20, anchor='center')

        self.address_label_image = tk.PhotoImage(file='/Users/zec/Desktop/Pic2/notiaddre.png')
        self.address_label = tk.Label(self, image=self.address_label_image, width=200, height=30, bg='#3C6739')
        self.address_label.place(x=110, y=80, anchor=CENTER)

        self.text_label2 = Label(self, text='a' , font=('Times New Roman', 24), compound ='center')
        self.text_label2.place(x=210, y=80, anchor='center')

        self.message_label_image = tk.PhotoImage(file='/Users/zec/Desktop/Pic2/notiteacher.png')
        self.message_label = tk.Label(self, image=self.message_label_image, width=210, height=30, bg='#3C6739')
        self.message_label.place(x=115, y=140, anchor=CENTER)

        self.text_label3 = Label(self, text='a' , font=('Times New Roman', 24), compound ='center')
        self.text_label3.place(x=205, y=140, anchor='center')

        self.zoom_label_image = tk.PhotoImage(file='/Users/zec/Desktop/Pic2/notizoom.png')
        self.zoom_label = tk.Label(self, image=self.zoom_label_image, width=120, height=40, bg='#3C6739')
        self.zoom_label.place(x=60, y=210, anchor=CENTER)

        self.text_label4 = Label(self, text='a' , font=('Times New Roman', 24), compound ='center')
        self.text_label4.place(x=125, y=210, anchor='center')
        


        self.notes_label_image = tk.PhotoImage(file='/Users/zec/Desktop/Pic2/notilec.png')
        self.notes_label = tk.Label(self, image=self.notes_label_image, width=190, height=40, bg='#3C6739')
        self.notes_label.place(x=110, y=250, anchor=CENTER)

        self.text_label5 = Label(self, text='a' , font=('Times New Roman', 24), compound ='center')
        self.text_label5.place(x=170, y=250, anchor='center')

        # Create buttons for Zoom and Lecture Notes

        self.zoom_button_image = tk.PhotoImage(file='/Users/zec/Desktop/Pic2/notijoin.png')
        self.zoom_button = tk.Button(self, image=self.zoom_button_image, width=150, height=40, bg='#3C6739', command=self.open_zoom)
        self.zoom_button.place(x=50, y=300, anchor=CENTER)

        self.notes_button_image = tk.PhotoImage(file='/Users/zec/Desktop/Pic2/notiview.png')
        self.notes_button = tk.Button(self, image=self.notes_button_image, width=150, height=40, bg='#3C6739', command=self.open_notes)
        self.notes_button.place(x=70, y=350, anchor=CENTER)


        # Create email entry and send button

        self.send_button_image = tk.PhotoImage(file='/Users/zec/Desktop/Pic2/SendEmail.png')
        self.send_button = tk.Button(self, image=self.send_button_image, command=self.send_email)
        self.send_button.place(x=230, y=410, anchor=CENTER)

        


    def open_zoom(self):
        zoom_link = "https://zoom.us/join"  # Replace with the actual Zoom link
        webbrowser.open(zoom_link)

    def open_notes(self):
        notes_link = "https://example.com/lecture-notes"  # Replace with the actual lecture notes link
        webbrowser.open(notes_link)


    def send_email(self):
        email = self.email_entry.get()

        subject = "Course Information"
        message = f"Course: {self.course_entry.get()}\n" \
                f"Classroom Address: {self.address_entry.get()}\n" \
                f"Teacher's Message: {self.message_entry.get()}\n"                f"Zoom Link: {self.zoom_entry.get()}\n" \
                f"Lecture Notes: {self.notes_entry.get()}\n"


        msg = EmailMessage()
        msg.set_content(message)
        msg['Subject'] = subject
        msg['From'] = "kanghunki@gmail.com"  # Replace with your email address
        msg['To'] = "kanghunki@gmail.com"

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login("kanghunki@gmail.com", "1")  # Replace with your email / pw
            server.send_message(msg)

        # Clear email entry
        self.email_entry.delete(0, tk.END)

# Create an instance of the CourseGUI class
app = CourseGUI()
app.mainloop()
