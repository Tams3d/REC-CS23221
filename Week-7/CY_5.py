vals = input().strip().split()
nums = []
for i in vals:
    if i not in nums:
        nums.append(i)
print("".join(nums))
