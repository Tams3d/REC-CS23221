n = int(input())
x = []

x = [int(input()) for i in range(n)]
pop = int(input())
print("List after appending elements:", x)
elem = x.pop(pop)
print("List after popping element:", x)
print("Popped element:", elem)
