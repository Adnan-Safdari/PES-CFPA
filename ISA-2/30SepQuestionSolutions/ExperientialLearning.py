"""
ADNAN SAFDARI
BCA-A SEMESTER 1
PES1UG24CA006
"""

# Storing user input in a variable to perform string manipulation
my_string = str(input("Enter a String: "))

"""
1) Return the string without any whitespace at the beginning or the end.
"""
print(f'\nStrip: {my_string.strip()}\n')


"""
2) Convert value fo text to upper case and lower case
"""
print(f'Uppercase: {my_string.upper()}')
print(f'LowerCase: {my_string.lower()}\n')


"""
3) Replace the character H with J in the text "Hello World"
"""
print(f'Replaced "H" with "J": {my_string.replace("H","J")}')


"""
4) Fix the following formatting
"""
age = 35
text = f"My name is John, and I am {age}"
print(text.format(age))

"""
5) Get the first cCharacter of the string "Hello World"
"""
print(f'The first character is: {my_string[0]}\n')

"""
6) What will be the output of the following?
"""
mySubject = "Computer Science"
print("These are gonna be the output of the following sub questions:")
print('  i:\t', mySubject[0:len(mySubject)])
print(' ii:\t', mySubject[-7:-1])
print('iii:\t', mySubject[::2])
print(' iv:\t', mySubject[len(mySubject)-1])
print('  v:\t', 2 * mySubject)
print(' vi:\t', mySubject[::-2])
print('vii:\t', mySubject[:3] + mySubject[3:])
print('viii:\t', mySubject.swapcase())
print(' ix:\t', mySubject.startswith("Comp"))
print('  x:\t', mySubject.isalpha())

"""
7) Write a program to accept string and display total number of alphabets
"""
result = ""
for i in my_string.strip().lower():
    if i in "abcdefghijklmnopqrstuvwxyz":
        result += i
print(f"The length of only alphabets is: {len(result)}")

"""
8) Write a program to accept a string and display each word and its length
"""
words = my_string.split()
for word in words:
    print(f"{word}:, Length: {len(word)}")

"""
9) Accept a string and display in reverse order
"""
print(f"Reversed String: {my_string[::-1]}")

"""
10) Accept a string and display the entire string with first and last character in uppercase
"""
my_string = my_string.strip().lower()
first_char = my_string[0].upper()  # Replacing the first character with uppercase
middle_char = my_string[1:-1]      # Getting the middle chars with string slicing
last_char = my_string[-1].upper()  # Replacing the last character with uppercase

result = first_char + middle_char + last_char  # Combining all the 3 together
print(result)

