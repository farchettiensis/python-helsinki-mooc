# Copy here code of line function from previous exercise and use it in your solution
def line(length, character):
    if character == "":
        character = "*"
    print(character[0] * length)

def shape(width, character, height, character2):
    i = 1
    while i <= width:
        line(i, character)
        i += 1
    for i in range(height):
        line(width, character2)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")
    shape(5, "", 2, "o")
    shape(2, "o", 4, "+")
    shape(3, ".", 0, ",")