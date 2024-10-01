"""
2) Write a python program to validate if the given string is palindrome or not
"""

# Converting input to lowercase to avoid conflicts (i.e. Malayalam != malayalaM)
my_string = str(input("Enter a String: ")).lower()

# 'is_palindrome' returns a Bool value
is_palindrome = my_string == my_string[::-1]

# Using ternary operator to print the output if condition is true
print((f"'{my_string}' is a Palindrome", f"'{my_string}' is not a Palindrome")[not is_palindrome])


# Guide: Ternary Operator -- https://www.geeksforgeeks.org/ternary-operator-in-python/