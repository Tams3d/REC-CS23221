from math import sqrt

n = int(input())

root = int(sqrt(n))

print("Odd" if root * root == n else "Even")
