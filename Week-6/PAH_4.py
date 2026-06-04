tup = ()
n = int(input())
for i in range(n):
    tup += ((input()),)
print(tuple(map(int, tup)))
print("".join(tup))
