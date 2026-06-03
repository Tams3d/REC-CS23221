sound = 343

ch = input()

if ch in ("d", "D"):
    time = float(input())
    print(f"Distance: {sound * time:.2f} m")
elif ch in ("b", "B"):
    size = float(input())
    print(f"Weight: {size * 5:.2f} lb")
elif ch in ("f", "F"):
    fly = float(input())
    d = float(input())
    print(f"Altitude: {fly * d:.2f} m")
else:
    print("Invalid")
