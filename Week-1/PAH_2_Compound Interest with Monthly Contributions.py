p = float(input())
r = float(input())
c = float(input())
m = int(input())

r = r / 100
n = 12
t = m / 12

a = p * (1 + r / n) ** (n * t) + c * (((1 + r / n) ** (n * t) - 1) / (r / n))

print(f"Final amount after {m} months: Rs. {a:.2f}")
