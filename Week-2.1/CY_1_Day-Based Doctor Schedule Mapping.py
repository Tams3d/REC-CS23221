n = int(input())
if n == 1 or n == 8 or n == 14:
    doc = "Smith"
elif n == 2 or n == 9:
    doc = "Johnson"
elif n == 3 or n == 10:
    doc = "Williams"
elif n == 4 or n == 11:
    doc = "Brown"
elif n == 5 or n == 12:
    doc = "Davis"
elif n == 6 or n == 13:
    doc = "Miller"
else:
    doc = "Wilson"

print(f"Doctor available on day {n} : Dr. {doc}")
