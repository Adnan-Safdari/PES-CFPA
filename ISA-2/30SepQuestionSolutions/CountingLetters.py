"""
Write a python program to calculate the occurrences of a letter in a String
"""

my_string = str(input("Enter your String: ")).lower()  # Converting to lowercase string
myList = []  # Defining an empty list to store the values

for letter in my_string:
    results = my_string.count(letter)  # count() func counts the occurrences of a letter
    myList.append(f"{letter}: {results}")  # appends adds more items to a list

# Converting to set to remove duplicates from the List
# Looping the print statement to get better looking output
for items in set(myList): 
    print(items)


