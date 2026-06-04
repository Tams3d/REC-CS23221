lst1 = lst2 = list(map(int, input().strip().split()))

print("List1:", lst1)

r = int(input())
if r in lst1:
    lst1.remove(r)
    print("List after removal: ", lst1)
else:
    print("Element not found in the list")

lst2 = list(map(int, input().strip().split()))
lst1.extend(lst2)
print("Final list: ", lst1)
