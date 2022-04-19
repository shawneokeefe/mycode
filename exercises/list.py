#!/usr/bin/env python3

import random

icecream= ["indentation", "spaces"]

students= ["Akino","Bai","Carlos","Dalton","Dan","Edith","Ethan","Isaiah","J","Jessica","John","Justin","Khalil","Nikk","Ramesh","Scotty","Sergio","Shawn"]

icecream.append(4)
#print([-1])


#input recorded as string
choice = int(input("Choose a student number between 0 and 17: "))
student_name= students[choice]

print(student_name + " " + str(choice))
print(students)
print(student_name + " always uses " + str(icecream[2]) + " "  + str(icecream[1]) + " to indent.")
print(f"{student_name} always uses {icecream[2]} {icecream[1]} to indent.")

