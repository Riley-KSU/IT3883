""""
username= [-1]
password= [-1]

def my_subtract(a=0,b=0):
    luckynumber = a+b
    num=a-b
    return luckynumber, num

c,d my_subtract()
print(c)
print(d)

score = [88, 92, 79, 85, 90]

def calculate_grade(score):
    average = sum(score) / len(score)
    print("Average:", average)
    highest = max(score)
    print("Highest", highest)
    lowest = min(score)
    print("Lowest", lowest)
    if average >= 90:
        print("Grade A")
    elif average >= 80:
        print("Grade B")
    elif average >= 70:
        print("Grade C")
    elif average >= 60:
        print("Grade D")
    else:
        print("Grade F")

calculate_grade(score)



import matplotlib as mpl
import numpy as np
import scipy as sp

a = [1,2,3]
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))


