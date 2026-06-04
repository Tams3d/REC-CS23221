def calculate_shipping(weight, destination):
    DOMESTIC_RATE = 5.0
    INTERNATIONAL_RATE = 10.0
    REMOTE_RATE = 15.0
    rate = None
    if destination == "Domestic":
        rate = DOMESTIC_RATE
    elif destination == "International":
        rate = INTERNATIONAL_RATE
    elif destination == "Remote":
        rate = REMOTE_RATE
    else:
        print("Invalid destination.")
        exit()
    return weight * rate


weight = float(input())
destination = input()
shipping_cost = calculate_shipping(weight, destination)
if shipping_cost is not None:
    print(
        f"Shipping cost to {destination} for a {weight} kg package: {shipping_cost:.2f}"
    )
