# Program Name: main.py (use the name the program is saved as)
# Course: IT3883/Section 01
# Student Name: Riley Dunevent
# Assignment Number: Assignment Number 1
# Due Date: 09/21/ 2026
# Purpose: What does the program do (in a few sentences)?
#The program prints a menue out with 4 options. Three of those options lets the user add text, clear it, or display
# it from the input buffer.
#The 4th option being exit the program.

# List Specific resources used to complete the assignment.
#I used the class D2L notes and W3 schools pyton material for stuff I was confused about still.

#Creates the string that will hold the input text
text = ""

#The meneu system that shows as the code runs
while True:
    print("-Input Buffer-")
    print("1. Append data to the input buffer")
    print("2. Clear the input buffer")
    print("3. Display the input buffer")
    print("4. Exit the program")

    # Ask the user to pick an option
    pick = input("Enter your choice (1-4): ")

    if pick == "1":
        user_text = input("Enter a string to append: ")
        text = text + user_text
        print("Data added to the input buffer.")
        # Option 2 - clears the buffer
    elif pick == "2":
        text = ""
        print("Input buffer has been cleared.")

    # Option 3 - Show what is currently stored in the buffer
    elif pick == "3":
        if text == "":
            print("The input buffer is empty.")
        else:
            print("Input Buffer:", text)

    # Option 4 - End the program
    elif pick == "4":
        print("Exiting program.")
        break

    # If they put anything other than 1-4 it ask them to try again
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")