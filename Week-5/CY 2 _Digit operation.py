n = int(input())

lst = list(map(int, input().strip().split()))
diff = lambda x, y: x - y
for i in lst:
    tot = 0
    prod = 1
    temp = i
    while temp:
        prod *= temp % 10
        tot += temp % 10
        temp //= 10

    print(diff(prod, tot))
