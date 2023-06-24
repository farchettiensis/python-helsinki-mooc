# Write your solution here
number = int(input("Please type in a number: "))
i = 1

while number >= i:
    if i+1 <= number:
        print(i+1)
    print(i)
    i += 2

""" Model solution:
number = int(input("Please type in a number: "))
index = 1

while index+1 <= number:
    print(index+1)
    print(index)
    index += 2

if index <= number:
    print(index)
"""