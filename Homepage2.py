from tkinter import *
import sqlite3
import tkinter.ttk as ttk
from tkinter import messagebox

class HomeWindow(Tk):
    def __init__(self, *main, **master):
        Tk.__init__(self, *main, **master)

        self.geometry('1280x720')
        self.resizable(0, 0)
        self.title('Student Login')
        self.config(bg='white')

        global USERNAME
        global PASSWORD
        USERNAME = StringVar()
        PASSWORD = StringVar()

        self._Header = PhotoImage(file="assets/image/HEADER5.png")
        self._HeaderLabel = Label(self, image=self._Header, height=300, width=300)
        self._HeaderLabel.place(x=500, y=2000)

        self._Footer = PhotoImage(file="assets/image/FOOTER.png")

        self._HeadLabel = Label(self, text='abc', width=100, height=100, bg='#3C6739').place(x=-5500, y=1000)
        self._background = PhotoImage(file='assets/image/Background.gif')
        self._image = PhotoImage(file='assets/image/HomeBackground.gif')

        self._Label1 = Label(self, image=self._background).place(x=0, y=0)
        self._Label2 = Label(self, image=self._image).place(relx=0.5, rely=0.5, anchor='center', height=450, width=920)

        self._HeaderLabel = Label(self, image=self._Header, text='Teacher', width=1277, height=80, bg='#3C6739').place(
            x=0, rely=0)
        self._FooterLabel = Label(self, image=self._Footer, height=40, width=1277, bg='#3C6739').place(x=0.5, y=677)

        # Load the dashboard image
        self._dashboard_image = PhotoImage(file='assets/image/Dashboard3.png')
        self._dashboard_label = Label(self, image=self._dashboard_image, height=588, width=190, bg='#3C6739')
        self._dashboard_label.place(x=0, y=85)

        # Create buttons for the dashboard
        self._profile_image = PhotoImage(file='assets/image/12.png')
        self._profile_image_label = Label(self, image=self._profile_image, width=100, height=100, bg='#3C6739')
        self._profile_image_label.place(x=40, y=100)
        
        self._Button1_image = PhotoImage(file='assets/image/Time.png')
        self._Button1_button = Button(self, image=self._Button1_image, width=170, height=50, bg='#3C6739')
        self._Button1_button.place(x=10, y=310)

        self._Button2_image = PhotoImage(file='assets/image/Discussion.png')
        self._Button2 = Button(self, image=self._Button2_image, width=160, height=40, bg='#3C6739')
        self._Button2.place(x=10, y=375)

        self._Button3_image = PhotoImage(file='assets/image/Zoom.png')
        self._Button3 = Button(self, image=self._Button3_image, width=150, height=40, bg='#3C6739')
        self._Button3.place(x=10, y=420)

        self._Button4_image = PhotoImage(file='assets/image/Lecture Notes.png')
        self._Button4 = Button(self, image=self._Button4_image, width=160, height=50, bg='#3C6739')
        self._Button4.place(x=10, y=250)


        self._Button5_image = PhotoImage(file='assets/image/Mater1.png')
        self._Button5 = Button(self, image=self._Button5_image, width=160, height=50, bg='#3C6739')
        self._Button5.place(x=3, y=470)

        self._Button6_image = PhotoImage(file='assets/image/Email.png')
        self._Button6 = Button(self, image=self._Button6_image, width=150, height=50, bg='#3C6739')
        self._Button6.place(x=10, y=520)

        self._Button7_image = PhotoImage(file='assets/image/log3.png')
        self._Button7 = Button(self, image=self._Button7_image, width=160, height=50, bg='#3C6739')
        self._Button7.place(x=10, y=620)


if __name__ == "__main__":
    app = HomeWindow()
    app.mainloop()