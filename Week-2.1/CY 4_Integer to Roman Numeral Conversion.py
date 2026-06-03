n = int(input())

values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
symbols = [
    "M",
    "CM",
    "D",
    "CD",
    "C",
    "XC",
    "L",
    "XL",
    "X",
    "IX",
    "V",
    "IV",
    "I",
]

ans = ""

for val, sym in zip(values, symbols):
    while n >= val:
        ans += sym
        n -= val

print(ans)
