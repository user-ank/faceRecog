import tkinter
from PIL import Image
import mysql.connector
import pandas as pd

# conn = mysql.connector.connect(
#                     host="localhost", username="root", password="", database="face_recognition_system")

df = pd.read_csv("Attendance_sheet.csv")

print("HEloo")