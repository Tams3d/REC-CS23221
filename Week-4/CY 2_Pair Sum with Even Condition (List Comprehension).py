nums = list(map(int, input().split()))
target = int(input())

pairs = [
    [x, y]
    for x in nums
    for y in nums
    if x != y and x + y == target and (x % 2 == 0 or y % 2 == 0)
]

for p in pairs:
    print(p)
