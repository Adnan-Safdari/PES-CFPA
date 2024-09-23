# - - - - - - - - - - - - - DEFINING STRINGS - - - - - - - - - - - - -
my_string1 = 'hello'
print(my_string1)  # Output: "hello"

my_string2 = "hello"
print(my_string2)  # Output: hello

my_string3 = '''Hello'''
print(my_string3)  # Output: Hello

my_string4 = """Hello"""
print(my_string4)  # Output: Hello

my_str = 'programming'
print('my_str=', my_str)  # Output: mystr= programming



# - - - - - - - - - - - - - SLICING STRINGS - - - - - - - - - - - - -

print('my_str[0]=', my_str[0])  # Output: my_str[0]= p
print('my_str[-1]=', my_str[-1])  # Output: my_str[-1]= g
print('my_str[1:5]=', my_str[1:5])  # Output: my_str[1:5]= rogr
print('my_str[5:-2]=', my_str[5:-2])  # Output: my_str[5:-2]= ammi

print(my_str[:2])  # output: pr
print(my_str[::2])  # output: pormig
# reverses the string
print(my_str[::-1])  # output:gnimmargorp

# - - - - - - - - - - - - - DELETING STRINGS - - - - - - - - - - - - -

temp_string = "Chalke Chalke"
print(temp_string)

del temp_string  # deleting the string
try:
    print(temp_string)  # Output: Chalke Chalke
except NameError:  # Handling the error as the string is deleted
    print("The var 'temp_string' does not exist")


# - - - - - - - - - - - - - HANDLING STRINGS WITH DIGITS - - - - - - - - - - - - -

string_filter_digits = "Hello World 123"

# Checking if all characters are a digit
result_filter_digits = all(char.isdigit() for char in string_filter_digits)
print(result_filter_digits)  # Output: False



