import sqlite3
import subprocess
from os import path

def connectTheDB():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS data (SourceName text, Username text, Password text)")
    cursor.execute("CREATE TABLE IF NOT EXISTS userLogin (Username text, UsernameLen int, Password text, PasswordLen int)") ## ------ maybe del? idk if thisll work
    connection.commit()
    connection.close()

def getLogin():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM userLogin")
    info = cursor.fetchall()
    connection.commit()
    connection.close()
    
    if len(info) == 0:
        return 0
    else:
        info = subprocess.run(['Login.exe', info[0][0], info[0][1], info[0][2], info[0][3],], stdout=subprocess.PIPE).stdout.decode('utf-8')
        info = str(info).split()
        return info

def addLogin(username, password):
    username = "\"" + username + "\""
    password = "\"" + password + "\""

    if path.exists("Login.exe"):
        # subprocess.call(["Login.exe", username, password])
        output = subprocess.run(['Login.exe', username, password], stdout=subprocess.PIPE).stdout.decode('utf-8')
    else:
        subprocess.call(["g++", "EncrDecr.h", "EncrDecr.cpp", "Login.cpp", "-o", "Login.exe"])
        # subprocess.call(["Login.exe", username, password])
        output = subprocess.run(['Login.exe', username, password], stdout=subprocess.PIPE).stdout.decode('utf-8')

    output = str(output).split()

    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    # cursor.execute("INSERT INTO userLogin VALUES (?, ?)", (username, password))
    cursor.execute("INSERT INTO userLogin VALUES (?, ?, ?, ?)", (output[0], output[1], output[2], output[3]))
    connection.commit()
    connection.close()

def add(sourceName, username, password):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO data VALUES (?,?,?)",(sourceName, username, password))
    connection.commit()
    row = cursor.execute("SELECT * FROM data ORDER BY SourceName DESC LIMIT 1")
    connection.close()
    # viewAll()
    return row

def remove(sourceName):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM data WHERE SourceName=?", (sourceName,))
    connection.commit()
    connection.close()

def search(sourceName):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM data WHERE SourceName=?", (sourceName,))
    row = cursor.fetchall()
    cursor.close()
    return row

def viewAll():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM data")
    rows = cursor.fetchall()
    cursor.close()
    return rows

def removeAll():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM data")
    connection.commit()
    connection.close()

def deleteData():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM userLogin")
    connection.commit()
    connection.close()

connectTheDB()