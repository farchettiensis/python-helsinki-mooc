# Write your solution here
word = input("Please type in a word: ")
character = input("Please type in a character: ")
index = word.find(character)
slice = word[index:index+3]

if len(slice) >= 3:
    print(slice)

