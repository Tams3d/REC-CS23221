from math import sqrt

n = int(input())
res = []
for i in range(1):
    a, b, c = map(int, input().split())
    d = b * b - 4 * a * c

    if d > 0:
        r1 = (-b + sqrt(d)) / (2 * a)
        r2 = (-b - sqrt(d)) / (2 * a)
        res.append((r1, r2))
    elif d == 0:
        res.append(((-b / (2 * a)),))
    else:
        r = -b / (2 * a)
        i = sqrt(-d) / (2 * a)
        res.append(((r, i), (r, -i)))

print(*tuple(res))
