# @Author: jiGg4
# @Date:   02-03-2017
# @Email:  jigg4@me.com
# @Filename: adduser.py
# @Last modified by:   jiGg4
# @Last modified time: 03-03-2017

from connectDatabaseV2 import *
import mysql.connec

def AddUserToDatabase(Name = "Anthony", Lastname = "Sherrill", MailAdd = "jigg4@me.com"):
    print("Adding user!")
    insert_new_user = (
    "INSERT INTO users (user_name, user_lastname, user_email) "
    "VALUES ({}, {}, {})".format(Name, Lastname, MailAdd))
    print(Name, Lastname, MailAdd, insert_new_user)
    cnx.commit()

AddUserToDatabase()


cur.close()
cnx.close()
