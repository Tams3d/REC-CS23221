n = int(input())
for i in range(n):
    marks = list(map(int, input().split()))
    tot = sum(marks)
    avg = tot / 5
    print("Total:", tot, "Average:", avg)
