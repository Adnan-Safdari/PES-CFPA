"""
Write a Python program to find whether the number is even or odd
"""

numberToCheck = int(input("Enter a number: "))

# If the remainder is '0' then the number is 'even', else it is 'Odd'
if (numberToCheck % 2) == 0:
    print("The following number is Even")

else:
    print("The following number is ODD")

