n = int(input())
names = []
prices = []
for _ in range(n):
    a, b = input().split()
    names.append(a)
    prices.append(b)

w1 = max(len(x) for x in names)
w2 = max(len(x) for x in prices)

for i in range(n):
    print(names[i].ljust(w1), prices[i].rjust(w2))
