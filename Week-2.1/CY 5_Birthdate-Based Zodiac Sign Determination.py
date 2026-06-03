day = int(input())
mon = input()

zod = ""

if (mon == "March" and day > 20) or (mon == "April" and day < 20):
    zod = "Aries"
elif (mon == "April" and day > 19) or (mon == "May" and day < 21):
    zod = "Taurus"
elif (mon == "May" and day > 20) or (mon == "June" and day < 21):
    zod = "Gemini"
elif (mon == "June" and day > 20) or (mon == "July" and day < 23):
    zod = "Cancer"
elif (mon == "July" and day > 22) or (mon == "August" and day < 23):
    zod = "Leo"
else:
    zod = "Other"

print("Your zodiac sign is " + zod)
