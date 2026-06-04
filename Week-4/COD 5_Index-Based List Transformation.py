n = int(input())

nums = []

nums = [int(input()) for i in range(n)]
nums.sort()
print("Original List:", nums)
nums[0] = 0

for i in range(2, n, 2):
    nums[i] = nums[i] ** 3
for i in range(1, n, 2):
    nums[i] = nums[i] ** 2
print("Replaced List:", nums)
