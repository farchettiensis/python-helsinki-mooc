# Write your solution here
times = int(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
groceries_weekly = float(input("How much money do you spend on groceries in a week? "))

daily = ((times * price) + groceries_weekly) / 7
weekly = (times * price) + groceries_weekly

print("Average food expenditure:")
print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")