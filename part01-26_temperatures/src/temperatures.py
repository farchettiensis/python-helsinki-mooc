# Write your solution here
temp_f = int(input("Please type in a temperature (F): "))
temp_c = (temp_f - 32) * 5 / 9

if temp_c < 0:
    print(f"{temp_f} degrees Fahrenheit equals {temp_c} degrees Celsius\n"
        "Brr! It's cold in here!")
print(f"{temp_f} degrees Fahrenheit equals {temp_c} degrees Celsius")