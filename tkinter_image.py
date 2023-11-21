import mysql.connector
from tkinter import Tk, Label
from PIL import ImageTk, Image

# Establish a connection to the MySQL database
cnx = mysql.connector.connect(
    host='your_host',
    user='your_username',
    password='your_password',
    database='your_database'
)

# Create a cursor object to execute SQL queries
cursor = cnx.cursor()

# Execute the query to fetch the image data
query = "SELECT image_data FROM images WHERE id = %s"  # Replace with the appropriate condition
values = (image_id,)  # Replace with the actual image ID or condition
cursor.execute(query, values)
result = cursor.fetchone()

# Retrieve the image data from the query result
image_data = result[0]

# Create a BytesIO object to read the image data
image_stream = io.BytesIO(image_data)

# Create an Image object using the PIL library
image = Image.open(image_stream)

# Create the Tkinter window
window = Tk()

# Create a Tkinter label to display the image
image_label = Label(window)

# Convert the Image object to a Tkinter PhotoImage object
photo = ImageTk.PhotoImage(image)

# Set the PhotoImage as the image label's image
image_label.config(image=photo)
image_label.pack()

# Run the Tkinter event loop
window.mainloop()

# Close the cursor and the connection
cursor.close()
cnx.close()