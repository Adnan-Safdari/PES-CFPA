"""
Write a program to find the leap year or not
"""

year = int(input("Enter the year to check: "))

if (year % 4) == 0:
    print(f"The year {year} is a Leap year")
else:
    print(f"The year {year} is not a Leap year")



