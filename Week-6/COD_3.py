n = int(input())
vals = list(map(int, input().split()))
for idx, val in enumerate(vals):
    vals[idx] **= idx
print(tuple(vals))
