text = input().strip()
nums = ""

for ch in text:
    if ch.isnumeric():
        nums += ch

nums = int(nums) if len(nums) else 0
tot = 0

while nums > 0:
    tot += nums % 10
    nums //= 10

if tot > 9:
    if str(tot) == str(tot)[::-1]:
        print(tot, "Palindrome")
    else:
        print(tot, "Not palindrome")
else:
    print(tot)
