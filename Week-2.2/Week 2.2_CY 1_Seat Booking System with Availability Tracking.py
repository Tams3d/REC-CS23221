seats = 10

while True:
    n = int(input())

    if n <= seats:
        seats -= n
        print(f"Booking {n} tickets")
        print(f"Remaining Seats: {seats}")

        if seats == 0:
            print("All seats have been booked. Thank you!")
            break
    else:
        print("Not enough seats available.")

    proceed = input()

    if proceed != "yes":
        print("Thank you for using our Ticket Booking System!")
        break
