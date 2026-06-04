num = int(input())


def sum_digits(num):
    tot = 0
    temp = num
    while temp != 0:
        tot += temp % 10
        temp //= 10
    return tot


sum = sum_digits(num)
print(sum)
