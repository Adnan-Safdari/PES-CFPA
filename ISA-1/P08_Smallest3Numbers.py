"""
Write a program to find the smallest of 3 numbers
"""

# Taking numbers input from the users
userInput1 = int(input("Enter 1st number: "))
userInput2 = int(input("Enter 2nd number: "))
userInput3 = int(input("Enter 3rd number: "))

myList = [userInput1, userInput2, userInput3]  # Adding those numbers to a list

smallest_value = 99999999999999999999999999999999999999999 # Creating a variable to hold the  value

for num in myList:
    if num < smallest_value:  # If the number is larger than the previous number then replace its value
        smallest_value= num

print(f"The smallest value is {smallest_value}")