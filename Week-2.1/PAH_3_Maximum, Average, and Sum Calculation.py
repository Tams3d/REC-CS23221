x = int(input())
y = int(input())
z = int(input())

mx = max((x, y, z))
tot = sum((x, y, z))

print(f"The maximum number is: {mx}")
print(f"Average: {tot / 3:.2f}")
print(f"Sum: {tot}")
