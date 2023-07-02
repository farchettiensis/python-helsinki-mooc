# Write your solution here
def no_shouting(string: list):
    no_upper = []
    
    for word in string:
        if word.isupper() == False:
            no_upper.append(word)
    return no_upper

if __name__ == "__main__":
    print(no_shouting(["The Joe Rogan Experience", "JRE", "PLUS ULTRA!", "PLUS ULTRA"]))