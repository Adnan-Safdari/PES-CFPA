"""
Write a program to check if it is divisible by 5
"""


num = int(input("Enter number to check divisibility: "))  # User inputs the number

operation = num % 5  # checking remainder [0=divisible, 1=not divisible]

if operation == 0:
    print(f"The number {num} is divisible by 5")

else:
    print(f"The number {num} is NOT divisible by 5")



