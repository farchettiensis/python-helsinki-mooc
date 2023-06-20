# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")
counter = 0
sum = 0
positive = 0
negative = 0
while True:
    number = int(input("Number: "))
    if number == 0:
        break
    if number > 0:
        positive += 1
    else:
        negative += 1
    counter += 1
    sum += number
print(f"Numbers typed in {counter}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {(sum / counter)}")
print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")