# Write your solution here
def first_word(f):
    end_index = f.find(" ")
    return f[:end_index]

def second_word(s):
    start_index = s.find(" ") + 1
    end_index = s.find(" ", start_index)
    if end_index == -1:
        end_index = len(s)
    return s[start_index:end_index]

def last_word(l):
    start_index = l.rfind(" ") + 1
    return l[start_index:]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))

""" Using the method split:
def first_word(sentence):
    return sentence.split(" ")[0]

def second_word(sentence):
    return sentence.split(" ")[1]

def last_word(sentence):
    return sentence.split(" ")[-1]
"""