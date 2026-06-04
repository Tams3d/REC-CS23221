n = int(input())
vals = set()
vals1 = set(map(int, input().split()))
for i in range(1, n):
    vals = set(map(int, input().split()))
    vals1 = vals1 - vals
print(sorted(vals1))
print(len(vals1))
