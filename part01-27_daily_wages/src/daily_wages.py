# Write your solution here
hourly_wage = float(input("Hourly wage: "))
hours_worked = float(input("Hours worked: "))
day_of_week = input("Day of the week: ")

daily_wage = hourly_wage * hours_worked

if day_of_week != "Sunday":
    print(f"Daily wages: {daily_wage} euros")
else:
    print(f"Daily wages: {daily_wage * 2} euros")