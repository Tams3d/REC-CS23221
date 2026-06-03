n = int(input())

for i in range(1, n + 1):
    left = " " * (n - i) + "* " * i
    right = " " * 2 * (n - i) + "* " * i
    print(left + right)
