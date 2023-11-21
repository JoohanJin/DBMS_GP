import os
import cv2
import mysql.connector
import PySimpleGUI as sg
import pickle
import datetime
import login_page
import sys
import PySimpleGUI as sg
import time

# GLOBAL VARIABLE
# DB connection 
db_connection = mysql.connector.connect(host="localhost", user="joe", passwd="1Q2w#E$R!!", database="project")
cursor = db_connection.cursor()

class HomePage:
    def __init__():
        return