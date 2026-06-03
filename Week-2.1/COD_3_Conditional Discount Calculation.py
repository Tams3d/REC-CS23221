day = input()
n = int(input())
amt = 200 * n

if day == "Monday" and n > 4:
    amt -= 150

print(f"Total amount to be paid: {amt}")
