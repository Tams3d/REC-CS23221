inter = set(range(1, 51))
combine = set()
for i in range(5):
    vals = set(map(int, input().split()))
    inter &= vals
    combine |= vals

print(sorted(inter, reverse=True))
print(sorted(combine - inter, reverse=True))
