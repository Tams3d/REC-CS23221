n = int(input())
nums = [int(x) for x in input().strip().split()]
ex = []
if n >= 6:
    ex = nums[-6:]
    ex.remove(ex[1])
    ex.remove(ex[3])
elif n == 5:
    ex = nums[:-1]
elif n == 4:
    ex = nums[1:-1]
else:
    ex = nums[:]

for i in range(len(ex)):
    print(ex[i] ** 3)
