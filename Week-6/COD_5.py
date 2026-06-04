n = int(input())
vals = []
for i in range(n):
    tup = eval(input())
    vals.extend(tup[1])
thres = int(input())
vals = list(filter(lambda x: x > thres, vals))
print(*vals)
