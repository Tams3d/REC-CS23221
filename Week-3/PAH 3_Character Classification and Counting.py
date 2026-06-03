s = input()
upr = 0
lwr = 0
digit = 0
spl = 0

for ch in s:
    if ch.isupper():
        upr += 1
    elif ch.islower():
        lwr += 1
    elif ch.isdigit():
        digit += 1
    else:
        spl += 1

print("Uppercase letters:", upr)
print("Lowercase letters:", lwr)
print("Digits:", digit)
print("Special characters:", spl)
