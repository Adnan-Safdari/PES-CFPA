"""
Write a program to print multiplication table
"""

number = int(input("Enter your number: "))

incrementVar = 1

while incrementVar <= 10:
    print(f"{number}x{incrementVar}={number*incrementVar}")
    incrementVar +=1
    