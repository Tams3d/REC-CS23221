n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

i = 0
while i < n:
    s = [a[i]]

    while i + 1 < n and a[i + 1] == a[i] + 1:
        i += 1
        s.append(a[i])

    print(f"({s[0]})" if len(s) == 1 else tuple(s))
    i += 1
