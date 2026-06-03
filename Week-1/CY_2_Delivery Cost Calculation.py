dist = int(input())
fare = 400

if dist > 3:
    dist -= 3
    fare += dist * 80

print(f"Number of full miles: {dist}")
print(f"Total cost of delivery: Rs. {fare}")
