alice = int(input())
bob = float(input())

print("Initial salaries:")
print(f"Alice's salary = {alice}")
print(f"Bob's salary = {bob}")

alice, bob = bob, alice

print("New salaries after swapping:")
print(f"Alice's salary = {alice:.1f}")
print(f"Bob's salary = {bob}")
