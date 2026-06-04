set1 = set(input().split())
set2 = set(input().split())
inter = set1 & set2
if inter:
    for i in sorted(inter):
        print(i, end=" ")
else:
    print("No common ingredients found.")
