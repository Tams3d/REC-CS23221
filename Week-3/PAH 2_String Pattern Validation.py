s = input().strip().lower()

vowels = "aeiou"

if s[0] in vowels:
    print("False")
else:
    ok = True
    for i in range(1, len(s)):
        if s[i] not in vowels and s[i - 1] not in vowels:
            ok = False
            break

    print("True" if ok else "False")
