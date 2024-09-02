"""Write a python program to print the employee salary depending on the following condition.
If exp < 1 year : 20,000
If exp b/w 1-5yrs: 35,000
If exp b/w 5-12yrs: 60,000
If exp more than 12 yrs: 1,20,000
"""

# We define the datatype as 'float' to accept decimal value as work experience
workExperience = float(input("Enter work experience: "))

salary = 0

if workExperience < 0:
    salary = "Invalid work experience"

elif workExperience >= 0 and workExperience < 1: # Below one year
    salary = 20000

elif workExperience >= 1 and workExperience < 5: # 1 to 5 years
    salary = 35000

elif workExperience >=5 and workExperience < 12: # 5 to 12 years
    salary = 60000

elif workExperience >= 12: # Above 12 years
    salary = 120000

print(f"Your salary is: {salary}")