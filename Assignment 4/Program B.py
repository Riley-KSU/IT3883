# Program Name: Program A.py
# Course: IT3883/Section 01
# Student Name: Riley Dunevent
# Assignment Number: Assignment 4
# Due Date: 11/05/2026
# Purpose: Receive a string from Program A, convert it to uppercase, and send the uppercase string back.
# Resources: Class notes and example Server.py from d2l and W3 schools.

import socket

# Creates the socket.
s = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

# Wait for Program A to connect.
s.bind(("127.0.0.1", 45000))
s.listen()
conn, addr = s.accept()

# Receive the text string from A.
data = conn.recv(256)
text = data.decode('utf-8')
print(text)

# Convert the text to uppercase and send it back to A.
text = text.upper()
byte_array = text.encode('utf-8')
conn.sendall(byte_array)

# Close the sockets.
conn.close()
s.close()