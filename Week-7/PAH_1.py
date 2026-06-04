nums = set()
n = int(input())
for i in range(n):
    vals = set(map(int, input().split()))
    nums = nums ^ vals

print(sorted(nums))
print(sum(nums))
