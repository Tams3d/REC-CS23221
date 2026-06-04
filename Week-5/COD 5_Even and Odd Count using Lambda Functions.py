n = int(input())

val = list(map(int, input().split()))
even = list(filter(lambda x: x % 2 == 0, val))
odd = list(filter(lambda x: x % 2, val))
print(len(even))
print(len(odd))
