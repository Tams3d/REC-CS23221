n = int(input())

s = sum(map(int, str(n)))

p = 1
while s**p < n:
    p += 1

if s**p == n:
    print(s, p)
else:
    print("Not possible")
