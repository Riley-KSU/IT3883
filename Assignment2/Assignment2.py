# Program Name: Assignment2.py
# Course: IT3883/Section 01
# Student Name: Riley Dunevent
# Assignment Number: Assignment 2
# Due Date: 10/2/2025
# Purpose: It reads the students scores from the document. It then calculates the student averages and print them highest to lowest.
# Resources: I used the class D2L notes and W3 schools pyton material for sorting that I was confused about.

# Create a list to store averages and names.
students = []

# Open the input file for reading.
input_file = open("Assignment2input.txt", "r")

# Read one student record at a time and separates the names and the scores.
for line in input_file:
    fields = line.split()
    total = 0

    # It loops through the scores after the names and converts them to numbers
    for score in fields[1:]:
        total = total + float(score)

    # Store the average first so sorting uses the grade.
    students.append([total / 6, fields[0]])

# Closes the file
input_file.close()

# Put the highest averages first.
students.sort(reverse=True)

# Prints names and averages with two decimal places.
for student in students:
    print(student[1], format(student[0], ".2f"))