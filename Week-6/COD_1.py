size = int(input())
val = list(map(int, input().split()))
n = int(input())

result = ()
if n > size:
    result = tuple(val)
else:
    for i in range(size):
        if (i + 1) % n != 0:
            result += (val[i],)

print(result)
