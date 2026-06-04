s = input().strip()
nums = list(map(int, s.strip("[]").split(",")))
pos = []
neg = []

for i in nums:
    if i < 0:
        neg.append(i)
    else:
        pos.append(i)

print("List = ", neg + pos)
