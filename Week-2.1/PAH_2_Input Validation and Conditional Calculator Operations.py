a = int(input())

if a < 1 or a > 9:
    print("Invalid Input")
else:
    y = input()

    if y == "n":
        print(a)
    elif y == "y":
        op = input()
        b = int(input())

        if op == "+":
            print(f"The result of the operation is: {a + b}")
        elif op == "-":
            print(f"The result of the operation is: {a - b}")
        elif op == "*":
            print(f"The result of the operation is: {a * b}")
        else:
            print("Invalid operation")
