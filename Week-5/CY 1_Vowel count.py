n = int(input())
lst = []
for i in range(n):
    lst.append(input())

maxvow = 0
maxstr = ""
isvow = lambda ch: ch in "aeiou"
for s in lst:
    vow = 0
    for ch in s:
        if isvow(ch):
            vow += 1

    if vow > maxvow:
        maxvow = vow
        maxstr = s

print(maxstr)
