"""
Write a program to find the largest of 3 numbers
"""

userInput1 = int(input("Enter 1st number: "))
userInput2 = int(input("Enter 2nd number: "))
userInput3 = int(input("Enter 3rd number: "))

myList = [userInput1, userInput2, userInput3]

largest_value = 0  # Creating a variable to hold the largest value

for num in myList:
    if num > largest_value:  # If the number is larger than the previous number then replace its value
        largest_value = num

print(f"The largest value is {largest_value}")