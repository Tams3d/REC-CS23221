w1 = input().lower().strip()
w2 = input().lower().strip()
com = set(w1) & set(w2)
print(sorted(com))
print(sorted(set(w1) ^ set(w2)))

print(set(w2).issubset(set(w1)))
print(not bool(set(w1) & set(w2)))
