num1, num2, num3 = map(float, input().split())

def find_max(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    return c

maximum = find_max(num1, num2, num3)
print(f"{maximum:.2f}", end="")
