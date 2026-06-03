low = int(input())
high = int(input())
low = max(2, low)
for num in range(low, high + 1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
