n = int(input())
arr = []
for i in range(n):
    vals = list(map(int, input().split()))
    arr.append(vals)

year = int(input()) - 1

print(f"{sum(arr[year]) / 12:.2f}")
