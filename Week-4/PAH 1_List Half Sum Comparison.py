n = int(input())
x = [int(i) for i in input().split()]
mid = n // 2
first = sum(x[:mid])
sec = sum(x[-mid:])
if first == sec:
    print("Balanced")
    print("Sum of first half:", first)
    print("Sum of second half:", sec)
else:
    print("Not Balanced")
    print("Original list:", *x)
