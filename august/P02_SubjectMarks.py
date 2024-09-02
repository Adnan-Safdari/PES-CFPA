"""
Write a python program to print the student result by taking 5 subjects
"""

print("Maximum Marks: 100")

# User inputting marks
subject1 = int(input("Enter subject 1 marks: "))
subject2 = int(input("Enter subject 2 marks: "))
subject3 = int(input("Enter subject 3 marks: "))
subject4 = int(input("Enter subject 4 marks: "))
subject5 = int(input("Enter subject 5 marks: "))

# Making sure that all the marks given is above 100
if subject1 > 100:
    print("ERROR: The marks provided for subject1 is above 100")
if subject2 > 100:
    print("ERROR: The marks provided for subject2 is above 100")
if subject3 > 100:
    print("ERROR: The marks provided for subject3 is above 100")
if subject4 > 100:
    print("ERROR: The marks provided for subject4 is above 100")
if subject5 > 100:
    print("ERROR: The marks provided for subject5 is above 100")

# Checking if the student has passed all subjects
if subject1 > 35 and subject2 > 35 and subject3 > 35 and subject4 > 35 and subject5 > 35:
    print("This student has passed")
else:
    print("This student has failed")

# Printing the student's percentage
marks_secured = subject1 + subject2 + subject3 + subject4 + subject5
total_marks = 100*5
perc = float((marks_secured/total_marks)*100)
print(f"The percentage obtained by the student is: {perc}")