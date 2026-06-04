n = int(input())

arr = list(map(int, input().split()))
bestdiff = 9999
bs1 = []
bs2 = []
for i in range(1, 2**n - 1):
    s1 = []
    s2 = []
    for j in range(n):
        if i & (1 << j):
            s1.append(arr[j])
        else:
            s2.append(arr[j])
    sum1 = sum(s1)
    sum2 = sum(s2)
    diff = abs(sum1 - sum2)
    if diff < bestdiff:
        bestdiff = diff
        bs1 = s1
        bs2 = s2

bs1.sort(reverse=True)
bs2.sort(reverse=True)

print(bs1)
print(bs2)
print(bestdiff)
