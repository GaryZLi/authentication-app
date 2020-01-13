import os
import subprocess
# import sys
import sqlite3

dirName = os.path.dirname(os.path.abspath(__file__))
subprocess.call(["g++", "EncrDecr.h", "EncrDecr.cpp", "Login.cpp", "-o", "Login.exe"])
# subprocess.call(["g++", "EncrDecr.cpp", "Login.cpp", "-o", "Login.exe"])
# subprocess.call(["g++", "Login.cpp", "-o", "Login.exe"])

# subprocess.call(["g++", "Login.cpp", "-o", "Login.exe"])

username = "}|{"
password = "bitch"
username = "\"" + username + "\""
password = "\"" + password + "\""

# subprocess.call(["Login.exe", username, password])
output = subprocess.run(['Login.exe', username, password], stdout=subprocess.PIPE).stdout.decode('utf-8')
output = str(output).split()
print("printing output:", output)
# print(output[1], output[2])

connect = sqlite3.connect("data.db")
cursor = connect.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS userLogin (Username text, UsernameLen text, Password text, PasswordLen text)")
# cursor.execute("INSERT INTO userLogin VALUES (?, ?, ?, ?)", (output[0], output[1], output[2], output[3]))
# cursor.execute("SELECT * FROM userLogin")
cursor.execute("DELETE FROM userLogin")
# cursor.execute("DROP TABLE userLogin")
connect.commit()
result = cursor.fetchall()
print(result)

# print("printing output split:", output)
# subprocess.call(["Login.exe", output[0], output[1], output[2], output[3]])

# 0xAAA #"! D 0x6AA5A F;*F< F

# subprocess.call(["./a.out"])

# a = input("pass: ")

# call(["Login.exe", a])
# subprocess.call(["Login.exe", "\"abc123\"", "\"password123\""])
# subprocess.call(["Login.exe", "\"0xAAAAAA klm;<=\"", "G"])

# # output = Popen([], stdout=PIPE)
# print(output)





# output = subprocess.run(['Login.exe', '}|{'], stdout=subprocess.PIPE).stdout.decode('utf-8')
# print(output)
os.remove("Login.exe")