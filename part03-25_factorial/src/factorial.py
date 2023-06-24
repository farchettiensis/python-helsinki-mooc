# Write your solution here
number = 1

while number > 0:
    number = int(input("Please type in a number: "))
    if number <= 0:
        print("Thanks and bye!")
        break
    i = number - 1
    factorial = number
    while i > 0:
        factorial = factorial * i
        i -= 1
    print(f"The factorial of the number {number} is {factorial}")
    
