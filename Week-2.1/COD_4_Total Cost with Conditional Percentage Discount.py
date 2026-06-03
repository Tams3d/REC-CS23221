n = int(input())

tot = 0

for i in range(n):
    bno = input()
    bname = input()
    price = float(input())
    tot += price

if tot > 750:
    tot -= tot * 0.05

print(f"Total cost: {tot:.1f}")
