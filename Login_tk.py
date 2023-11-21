from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


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

<<<<<<< HEAD
# Create labels
username_image = ImageTk.PhotoImage(Image.open("/Users/zec/Desktop/Pic2/User.png"))
label_username = Label(root, image=username_image, height=45, width=90, bg='gray')
label_username.place(x=170, y=330, anchor=CENTER)

password_image = ImageTk.PhotoImage(Image.open("/Users/zec/Desktop/Pic2/PW.png"))
label_password = Label(root, image=password_image, height=45, width=90, bg='white')
label_password.place(x=170, y=430, anchor=CENTER)

# Create input fields
entry_username = Entry(root, bg="white", relief=FLAT)
entry_username.place(x=170, y=370, anchor=CENTER)


entry_password = Entry(root, bg="white", show="*", relief=FLAT)
entry_password.place(x=170, y=470, anchor=CENTER)

# Create login button
login_image = ImageTk.PhotoImage(Image.open("/Users/zec/Desktop/Pic2/login2.png"))
login_button = Button(root, image=login_image, height=40, width=90, bg='white')
login_button.place(x=420, y=450, anchor=CENTER)
=======
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
        login_button = Button(self.root, image=login_image, command=self.login, height=40, width=90, bg='white')
        login_button.place(x=380, y=450, anchor=CENTER)
>>>>>>> a6fb084 (yeah)

        # Load image for another button
        image = ImageTk.PhotoImage(Image.open("assets/image/loginface.png"))

<<<<<<< HEAD
# Create button with image and circular border
image_button = Button(root, image=image, command=login, height=78, width=100, bg='white')
image_button.place(x=420, y=350, anchor=CENTER)
=======
        # Create button with image and circular border
        image_button = Button(self.root, image=image, height=78, width=100, bg='white')
        image_button.place(x=380, y=350, anchor=CENTER)
>>>>>>> a6fb084 (yeah)

        self.root.mainloop()
    
    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "3035661360" and password == "12345":
            messagebox.showinfo("Login Success", "Log In Success")
        else:
            messagebox.showerror("Login Error", "Incorrect")

if __name__=="__main__":
    LogInPage()