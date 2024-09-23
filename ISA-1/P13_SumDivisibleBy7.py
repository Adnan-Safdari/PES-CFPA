"""
Write a python program to find the numbers and calculate the sum 
between 100 and 200 which are divisible by 7
"""
# --- Method 1 ---
print(sum(list(range(105, 201, 7))))

# ---Method 2 ---
startRange = 100
endRange = 200


# Getting list of numbers between 100 and 200
numbers = []
while startRange < endRange:
    numbers.append(startRange)
    startRange +=1

sum = 0
for n in numbers:
    if (n%7) == 0:
        sum+=n

print(f"The sum of numbers divisible by 7 between 100 and 200 is: {sum}")
