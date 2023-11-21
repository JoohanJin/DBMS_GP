import tkinter as tk
from tkinter import *
import webbrowser
import smtplib
from email.message import EmailMessage

class CourseGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('300x370')
        self.resizable(0, 0)
        self.title('Notifications')
        self.config(bg='#333333')



        self._background = PhotoImage(file='/Users/zec/Desktop/Pic2/Notiback2.png')
        self._Label1 = Label(self, image=self._background).place(x=0, y=0)

        # Create labels for course information
        label_font = ("Times New Roman", 14, "bold")  # Set the font for the labels

        self._course_label_image = tk.PhotoImage(file='/Users/zec/Desktop/Pic2/noticourse.png')
        self.course_label = tk.Label(self, image=self._course_label_image, width=150, height=40, bg='#3C6739')
        self.course_label.place(x=10, y=20)
        self.course_label.pack()
        
        self.address_label_image = tk.PhotoImage(file='/Users/zec/Desktop/Pic2/notiaddre.png')
        self.address_label = tk.Label(self, image=self.address_label_image, width=200, height=30, bg='#3C6739')
        self.address_label.place(x=10, y=30)
        self.address_label.pack()
        
        self.message_label_image = tk.PhotoImage(file='/Users/zec/Desktop/Pic2/notiteacher.png')
        self.message_label = tk.Label(self, image=self.message_label_image, width=210, height=30, bg='#3C6739')
        self.message_label.place(x=100, y=40)
        self.message_label.pack()
        
        self.zoom_label_image = tk.PhotoImage(file='/Users/zec/Desktop/Pic2/notizoom.png')
        self.zoom_label = tk.Label(self, image=self.zoom_label_image, width=120, height=40, bg='#3C6739')
        self.zoom_label.place(x=10, y=50)
        self.zoom_label.pack()
        
        self.notes_label_image = tk.PhotoImage(file='/Users/zec/Desktop/Pic2/notilec.png')
        self.notes_label = tk.Label(self, image=self.notes_label_image, width=190, height=40, bg='#3C6739')
        self.notes_label.place(x=80, y=60)
        self.notes_label.pack()
        
        # Create buttons for Zoom and Lecture Notes
        
        self.zoom_button_image = tk.PhotoImage(file='/Users/zec/Desktop/Pic2/notijoin.png')
        self.zoom_button = tk.Button(self, image=self.zoom_button_image, width=150, height=40, bg='#3C6739')
        self.zoom_button.place(x=10, y=20)
        self.zoom_button.pack()
        
        self.notes_button_image = tk.PhotoImage(file='/Users/zec/Desktop/Pic2/notiview.png')
        self.notes_button = tk.Button(self, image=self.notes_button_image, width=150, height=40, bg='#3C6739', command=self.open_notes)
        self.notes_button.place(x=10, y=20)
        self.notes_button.pack()
        
        # Create email entry and send button
        entry_font = ("Times New Roman", 12)  # Set the font for the entry widget
        
        self.email_entry = tk.Entry(self, font=entry_font)
        self.email_entry.pack()
        
        self.send_button = tk.Button(self, text="Send Email", command=self.send_email)
        self.send_button.pack()
        
    def open_zoom(self):
        zoom_link = "https://zoom.us/join"  # Replace with the actual Zoom link
        webbrowser.open(zoom_link)
        
    def open_notes(self):
        notes_link = "https://example.com/lecture-notes"  # Replace with the actual lecture notes link
        webbrowser.open(notes_link)
        


    def send_email(self):        # Replace the email address / create App Password in Gmail for new email. 
        email = self.email_entry.get() #https://www.youtube.com/watch?v=hSnd8iYBiIg 

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
        self.email_entry.delete(0, tk.END)

# Create an instance of the CourseGUI class
app = CourseGUI()
app.mainloop()





