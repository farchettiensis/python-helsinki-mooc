# Write your solution here
year = int(input("Year: "))
initial_year = year

while True:
    year += 1
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        break
print(f"The next leap year after {initial_year} is {year}")