a = float(input())
b = float(input())
c = float(input())

if a == b == c:
    print("The triangle is classified as Equilateral")
elif a == b or b == c or a == c:
    print("The triangle is classified as Isosceles")
else:
    print("The triangle is classified as Scalene")
