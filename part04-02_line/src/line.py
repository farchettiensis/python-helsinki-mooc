# Write your solution here
def line(length, character):
    if character == "":
        character = "*"
    print(character[0] * length)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")
    line(10, "God Usopp ")
    line(3, "")