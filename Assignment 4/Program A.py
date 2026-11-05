# Program Name: Program A.py
# Course: IT3883/ Section 01
# Student Name: Riley Dunevent
# Assignment Number: Assignment 4
# Due Date: 11/05/2026
# Purpose: Send a string to Program B and display its response.
# Resources: Class notes and example Client.py from d2l and W3 schools.

import socket

# Create the socket.
s = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

# Connects it to Program B.
s.connect(("127.0.0.1", 45000))

# Ask for a text string and send it to program B.
text = input("Enter a string: ")
byte_array = text.encode('utf-8')
s.sendall(byte_array)

# Receive and print the response from Program B.
print("Uppercase string:", s.recv(256).decode('utf-8'))
s.close()