n = int(input())
a = list(map(int, input().split(",")))
print([max((y for y in a if x % y == 0 and y < x), default=-1) for x in a])
