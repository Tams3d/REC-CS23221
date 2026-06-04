lst1 = list(map(int, input().split()))[:-1]
lst2 = list(map(int, input().split()))
print(sorted(set(lst1) | set(lst2)))
