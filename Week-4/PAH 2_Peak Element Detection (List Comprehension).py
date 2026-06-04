x = [int(i) for i in input().split()]
peak = []
for i in range(len(x) - 2):
    if x[i] < x[i + 1] > x[i + 2]:
        peak.append(x[i + 1])

print("Peaks:", peak)
