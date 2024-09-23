"""
EXTRA: Write a program to get the list of all leap years between the years 1990 and 2050
"""

year = 1990  # starting range

while year <= 2050:  # Specifing ending range
    if (year % 4)==0: # Checking if it is a leap year
        print(year)
    year +=1  # Incrementing the year