import mysql.connector
from tkinter import Tk, Label
from PIL import ImageTk, Image
import io

# Establish a connection to the MySQL database
db_connection = mysql.connector.connect(host="localhost", user="joe", passwd="1Q2w#E$R!!", database="project")

# Create a cursor object to execute SQL queries
cursor = db_connection.cursor()

images = [
    "timetable_1.png",
    "timetable_2.png",
    "timetable_3.png",
    "timetable_4.png",
    "timetable_5.png",
    "timetable_6.png",
    "timetable_7.png",
    "timetable_8.png"
]

student_id = [
    "3035678110",
    "3035678111",
    "3035678112",
    "3035678113",
    "3035678114",
    "3035678115",
    "3035678116",
    "3035678117"
]

# for i in range(len(images)):
#     photo_path = f"assets/image/{images[i]}"
#     with open(photo_path, "rb") as photo_file:
#         photo_data = photo_file.read()
#     query = "INSERT INTO TimeTable Values (%s, %s, %s)"
#     values = (i, student_id[i], photo_data,)

#     cursor.execute(query, values)
#     db_connection.commit()

# cursor.close()
# db_connection.close()

    

# Execute the query to fetch the image data
query = "SELECT time_table_image FROM TimeTable WHERE student_id = %s"  # Replace with the appropriate condition
values = ("3035678117",)  # Replace with the actual image ID or condition
cursor.execute(query, values)
result = cursor.fetchone()

# print(result)


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
db_connection.close()