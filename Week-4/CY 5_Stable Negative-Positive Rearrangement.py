txt = eval(input())

neg = [x for x in txt if x < 0]
pos = [x for x in txt if x >= 0]

res = neg + pos
print(repr(res).replace(" ", ""))
