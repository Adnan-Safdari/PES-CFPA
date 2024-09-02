"""
Write a python program to take 10 inputs from the user using while loop
"""

num = 1
userResponses = []  # List to store user inputs

while num <= 10:
    userInput = input(f"Enter your {num} input: ")
    userResponses.append(userInput)  # Appending user inputs to our list
    num +=1

print(f"The user inputted: {userResponses}")