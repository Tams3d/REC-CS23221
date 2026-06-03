fn = input()
ln = input()
role = input()
portal = input()

domain = f"admin.{portal}" if role == "admin" else f"{portal}"
print(f"{fn[0]}{ln}@{domain}.com".lower())
