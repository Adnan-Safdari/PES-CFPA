"""
Write a program to find if a character is a vowel or consonant
"""

charInput = input("Enter your character: ")
# Getting the first character if the user has inputted multiple characters
# Converting it to lower case
char = charInput[0].lower() 
vowels = ['a', 'e', 'i', 'o', 'u']

if char in vowels:
    print(f"{char} is a vowel")
else:
    print(f"{char} is a consonant")