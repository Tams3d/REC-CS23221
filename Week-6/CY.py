n = int(input())

vals = list(map(int, input().split()))
tup = ()
for i in range(1, n):
    tup += (abs(vals[i - 1] - vals[i]),)
print(tup)
