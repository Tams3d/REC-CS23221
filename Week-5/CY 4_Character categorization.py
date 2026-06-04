def analyze_string(txt):
    upr = 0
    lwr = 0
    digit = 0
    spl = 0
    for i in txt:
        if i.isnumeric():
            digit += 1
        if i.islower():
            lwr += 1
        if i.isupper():
            upr += 1
        if not i.isalnum():
            spl += 1

    return upr, lwr, digit, spl


input_string = input()
uppercase_count, lowercase_count, digit_count, special_count = analyze_string(
    input_string
)

print("Uppercase letters:", uppercase_count)
print("Lowercase letters:", lowercase_count)
print("Digits:", digit_count)
print("Special characters:", special_count)
