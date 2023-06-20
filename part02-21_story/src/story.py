# Write your solution here
story = ""
previous_word = ""

while True:
    word = input("Please type in a word: ")
    
    if (word == "end"):
        break
    elif (previous_word == word):
        break

    story += word + " "
    previous_word = word

print(story)

