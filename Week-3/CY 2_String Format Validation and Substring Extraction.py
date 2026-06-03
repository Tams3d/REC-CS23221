n = int(input())
codes = []

for _ in range(n):
    s = input()

    if (
        len(s) == 14
        and s[0] == "("
        and s[4] == ")"
        and s[5] == " "
        and s[9] == "-"
        and s[1:4].isdigit()
        and s[6:9].isdigit()
        and s[10:].isdigit()
    ):
        codes.append(s[1:4])

print("Valid area codes:", ",".join(codes))
