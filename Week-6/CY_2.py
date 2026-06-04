n = int(input())
vals = list(map(int, input().split()))
prev = vals[0]
for i in range(1, n):
    vals[i] = vals[i] * prev
    prev = vals[i]
print(tuple(vals))
