n = int(input())
nums = [int(input()) for _ in range(n)]
thres = float(input())

harm = lambda num: (
    0 if "0" in str(num) else len(str(num)) / sum(1 / int(d) for d in str(num))
)

print([i for i in nums if harm(i) > thres])
