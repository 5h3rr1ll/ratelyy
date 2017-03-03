# @Author: jiGg4
# @Date:   03-03-2017
# @Email:  jigg4@me.com
# @Filename: connectDatabase.py
# @Last modified by:   jiGg4
# @Last modified time: 03-03-2017



import mysql.connector
from mysql.connector import errorcode

config = {
    "user" : "d025764e",
    "password" : "03121982",
    "host" : "85.13.154.99",
    "database" : "d025764e"
}

cnx = cur = None


try:
    cnx = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cur = cnx.cursor()
    cur.execute("show databases;")
    for row in cur.fetchall():
        print(row)
