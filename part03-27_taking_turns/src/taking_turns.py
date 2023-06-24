# Write your solution here
number = int(input("Please type in a number: "))
i = 1

while number >= i:
    if number == i:
        print(i)
        break
    print(i)
    print(number)
    i += 1
    number -= 1