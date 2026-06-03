n = int(input())

for i in range(n):
    print(" " * (n - i - 1), end="")

    val = 1
    for j in range(i + 1):
        print(val, end="" if j == i else " ")
        val = val * (i - j) // (j + 1)

    print()
