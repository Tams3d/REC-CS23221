n = int(input())
temp = n
fact = 1
while temp:
    fact *= temp
    temp -= 1

print(f"The factorial of {n} is: {fact}")
