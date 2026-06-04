n = int(input())
a = tuple(map(int, input().split()))

m = int(input())
b = tuple(map(int, input().split()))

result = set()

for x in set(a) & set(b):  
    if (a.count(x) + b.count(x)) % 2 != 0:
        result.add(x)

if result:
    print(tuple(sorted(result)))
else:
    print("No common elements found.")
