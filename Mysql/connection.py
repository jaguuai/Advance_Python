import mysql.connector
from datetime import datetime
# Eğer datetime from yapmazsak asagıda datime.datetime yapmayı unutma
connection=mysql.connector.connect(
  host="localhost",
  user="root",
  password="", 
  # it deleted for securıty
  database="schooldb"
 )