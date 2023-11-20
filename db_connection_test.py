from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import ctypes
import time
import mysql.connector
from functools import partial
import re
from datetime import datetime
import webbrowser

import smtplib
from email.mime.text import MIMEText
## import packages for send_email()

ID = 10;


db_connection = mysql.connector.connect(host="localhost", user="joe", passwd="1Q2w#E$R!!", database="project");
# date = datetime.date();
# now = datetime.date.now();
now = datetime.now()
current_date = now.strftime("%H:%M:%S");
cursor = db_connection.cursor();


# command = "SELECT id, name, date_of_join FROM test";
input_command = f"SELECT id, name, date_of_join FROM test WHERE id = {ID}";

name = cursor.execute(input_command);
result = cursor.fetchall(); # mysql_connect save its result in the type of <list>.
print(result);

edit_command = "UPDATE test SET date_of_join = %s WHERE id = %s";

name = cursor.execute(edit_command, (now.date(), ID));
db_connection.commit();


name = cursor.execute(input_command);
result = cursor.fetchall(); # mysql_connect save its result in the type of <list>.

print(result);
