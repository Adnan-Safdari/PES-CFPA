""" Write logical expresions corresponding to the following statements """

# [a] - The sum of 20 and -10 is less than 12
a_result = (20+(-10)) < 12
print(f"The output of 'a' is: {a_result}")

# [b] - num3 is not more than than 24
num3 = 5
b_result = num3 < 24
print(f"The output of 'b' is: {b_result}")

# [c] -  6.75 is between the values of integers num1 and num2
num1 = 5.00
num2 = 10.00
c_result = num1 < 6.75 < num2
print(f"The output of 'c' is: {c_result}")

# [d] -  The string ‘middle’ is larger than the string ‘first’ and smaller than the string ‘last’.
d_result = 'first' < 'middle' < 'last'
print(f"The output of 'd' is: {d_result}")

# [e] - List stationery is empty
stationery = []
e_result = not stationery
print(f"The output of 'e' is: {e_result}")


