n = int(input())
lst1 = list(map(int, input().split(",")))
lst2 = list(map(int, input().split(",")))
vals = []
for i in range(n):
    vals.append(lst1[i] + lst2[i])


print(tuple(vals))
