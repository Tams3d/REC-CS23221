n = int(input())
string = input().split()

print(*string[-2:], *string[:-2])
