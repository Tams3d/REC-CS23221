height = float(input())
waist = float(input())

bf = 64 - (20 * (height / waist))
print(f"{bf:.2f}%")

if 2 <= bf <= 5:
    print("Essential fat")
elif 6 <= bf <= 13:
    print("Athletes")
elif 14 <= bf <= 17:
    print("Fitness")
elif 18 <= bf <= 24:
    print("Average")
else:
    print("Obese")
