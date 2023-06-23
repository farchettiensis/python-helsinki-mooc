# Write your solution here
string = input("Please type in a string: ").lower()
letters = ["a", "e", "o"]

i = 0
while i < len(letters):
    letter = letters[i]
    if letter in string:
        print(f"{letter} found")
    else:
        print(f"{letter} not found")
    i += 1
