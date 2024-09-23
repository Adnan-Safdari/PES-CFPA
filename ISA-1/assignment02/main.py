
def swapVariables(a, b):
    """Swapping variables without 3rd variable"""
    print("- - - - - PROGRAM 1 (a)- - - - - -")
    print(f"Value before swapping a: {a}, b: {b}")
    a, b = b, a
    print(f"Value  after swapping a: {a}, b: {b}")
    return a, b


def swapVariablesWithVariables(a, b):
    """Swapping variables with 3rd variable"""
    print("- - - - - PROGRAM 1 (b) - - - - - -")
    print(f"Value before swapping a: {a}, b: {b}")
    c = a
    a = b
    b = c

    print(f"Value  after swapping a: {a}, b: {b}")
    return a, b


def goodMorningLoop():
    """Swapping variables with 3rd variable"""
    print("- - - - - PROGRAM 2 - - - - - -")
    times = int(input(f"How many times do you want to get wished 'Good Morning?:"))
    myString = "Good Morning! \n"
    print(times * myString)


swapVariables(10 ,6)
swapVariablesWithVariables(50, 100)
goodMorningLoop()
