"""
Write a python program to check whether the login and password both are correct
"""

CorrectUsername = "admin"
CorrectPassword = "admin"

username = input("Enter your username: ")
password = input("Enter your password: ")

if (username == CorrectUsername) and (password == CorrectPassword):
    print("Login successfull")
else:
    print("Wrong password. Login Failed!")