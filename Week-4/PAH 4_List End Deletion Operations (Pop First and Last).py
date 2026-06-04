n = int(input())
nums = [int(input()) for i in range(n)]

print("List after appending elements:", nums)
last = nums.pop()
print("List after popping last element:", nums)
print("Popped element:", last)
first = nums.pop(0)
print("List after popping first element:", nums)
print("Popped element:", first)
