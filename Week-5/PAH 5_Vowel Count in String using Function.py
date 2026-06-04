lst = list(map(int, input().split()))
a = lambda x: x**2
b = lambda y: y**3
print(list(map(a, lst)))
print(list(map(b, lst)))
