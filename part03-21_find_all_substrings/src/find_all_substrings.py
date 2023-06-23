# Write your solution here
string = input("Please type in a word: ")
character = input("Please type in a character: ")
index = string.find(character)

while (index != -1 and len(string) >= index+3):
    if (string[0] == character):
        print(string[index:index+3])
    string = string[1:]
    index = string.find(character)

""" Model solution:
word = input("Please type in a word: ")
character = input("Please type in a character: ")
 
index = 0
 
while index + 3 <= len(word):
    if word[index] == character:
        print(word[index:index+3])
    index += 1
"""