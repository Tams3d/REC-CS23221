vals = set(map(int, input().split()))
m = int(input())

print("{" + repr(sorted(vals, reverse=True))[1:-1], "}")
if m == 1:
    print(max(vals))
elif m == 2:
    print(min(vals))
elif m == 3:
    n = int(input())
    if n in vals:
        vals.remove(n)
    print("{" + repr(sorted(vals, reverse=True))[1:-1], "}")
else:
    print("Invalid choice")
