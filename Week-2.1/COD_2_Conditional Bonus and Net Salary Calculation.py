salary = float(input())
years = int(input())
bonus = float(input())
tax = float(input())

net_bonus = 0
if years > 5:
    net_bonus = bonus / 100 * salary
    print(f"You have earned a bonus oof {net_bonus:.1f} units.")
else:
    print("orry, you are not eligible for a bonus.")

tax_amt = tax / 100 * (salary + net_bonus)
net_salary = salary + net_bonus - tax_amt

print(f"Tax Amount: {tax_amt:.1f} units")
print(f"Net Salary: {net_salary:.1f} units")
