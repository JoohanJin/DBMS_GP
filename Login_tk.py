from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "3035661360" and password == "12345":
        messagebox.showinfo("Login Success", "Log In Success")
    else:
        messagebox.showerror("Login Error", "Incorrect")

root = Tk()
root.title("Login Form")
root.geometry("550x500")  # Set the size of the window

# Load background image
bg_image = ImageTk.PhotoImage(Image.open("/Users/zec/Desktop/Pic2/HKU.png"))
bg_label = Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create labels
username_image = ImageTk.PhotoImage(Image.open("/Users/zec/Desktop/Pic2/User.png"))
label_username = Label(root, image=username_image, height=45, width=90, bg='gray')
label_username.place(x=130, y=330, anchor=CENTER)

password_image = ImageTk.PhotoImage(Image.open("/Users/zec/Desktop/Pic2/PW.png"))
label_password = Label(root, image=password_image, height=45, width=90, bg='white')
label_password.place(x=130, y=430, anchor=CENTER)

# Create input fields
entry_username = Entry(root, bg="white", relief=FLAT)
entry_username.place(x=130, y=370, anchor=CENTER)


entry_password = Entry(root, bg="white", show="*", relief=FLAT)
entry_password.place(x=130, y=470, anchor=CENTER)

# Create login button
login_image = ImageTk.PhotoImage(Image.open("/Users/zec/Desktop/Pic2/login2.png"))
login_button = Button(root, image=login_image, command=login, height=40, width=90, bg='white')
login_button.place(x=380, y=450, anchor=CENTER)

# Load image for another button
image = ImageTk.PhotoImage(Image.open("/Users/zec/Desktop/Pic2/loginface.png"))

# Create button with image and circular border
image_button = Button(root, image=image, command=login, height=78, width=100, bg='white')
image_button.place(x=380, y=350, anchor=CENTER)

root.mainloop()
