# - - - - - - - - - - - - - DEFINING STRINGS - - - - - - - - - - - - -
my_string1 = 'hello'
print(my_string1)

my_string2 = "hello"
print(my_string2)

my_string3 = '''Hello'''
print(my_string3)

my_string4 = """Hello"""
print(my_string4)

my_str = 'programming'
print('my_str=', my_str)

# - - - - - - - - - - - - - SLICING STRINGS - - - - - - - - - - - - -

print('my_str[0]=', my_str[0])  # prints the first element
print('my_str[-1]=', my_str[-1])  # prints the last element
print('my_str[1:5]=', my_str[1:5])  # prints the 2nd and 6th element
print('my_str[5:-2]=', my_str[5:-2])  # prints the 6th to 2nd last element

print(my_str[:2])  # output: "pr"
print(my_str[::2])  # output: "pormig"
print(my_str[::-1])  # reverses the string

# - - - - - - - - - - - - - DELETING STRINGS - - - - - - - - - - - - -

temp_string = "Chalke Chalke"
print(temp_string)

del temp_string  # deleting the string
try:
    print(temp_string)
except NameError:  # Handling the error as the string is deleted
    print("The var 'temp_string' does not exist")


# - - - - - - - - - - - - - HANDLING STRINGS WITH DIGITS - - - - - - - - - - - - -

string_filter_digits = "Hello World 123"

# Checking if all characters are a digit
result_filter_digits = all(char.isdigit() for char in string_filter_digits)
print(result_filter_digits)  # Output: False



