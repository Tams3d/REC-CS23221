def find_odd_numbers(num):
    print(*list(range(1, num + 1, 2)), sep=", ")


user_input = input()
numbers = map(int, user_input.split())

find_odd_numbers(*numbers)
