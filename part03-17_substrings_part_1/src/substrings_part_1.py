# Write your solution here
string = input("Please type in a string: ")
length = len(string)
i = 0

while i <= length:
    print(string[0:i])
    i += 1