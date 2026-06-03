from math import factorial

n = int(input())

fact = factorial(n)
print(fact)

tot = 0
while fact:
    tot += fact % 10
    fact //= 10

print(tot)
