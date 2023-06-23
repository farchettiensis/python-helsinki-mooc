# Write your solution here
sentence = input("Please type in a sentence: ")
length = len(sentence)
index = 0

while index < length and sentence[index] == " ":
    index += 1

while index < length:
    print(sentence[index])

    while index < length and sentence[index] != " ":
        index += 1

    while index < length and sentence[index] == " ":
        index += 1

""" Crap solution:
sentence = input("Please type in a sentence: ")
index = 0

# sentence = "The Rise and Fall of Ziggy Stardust"

def retrieve_and_print_word(index):
    while index < len(sentence) and sentence[index] == " ":
        index += 1
    if index < len(sentence):
        print(sentence[index])
    return sentence.find(" ", index) + 1 if sentence.find(" ", index) != -1 else len(sentence)

index = 0
while index < len(sentence):
    index = retrieve_and_print_word(index)
"""

