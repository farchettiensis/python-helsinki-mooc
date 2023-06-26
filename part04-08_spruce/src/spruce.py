# Write your solution here
def spruce(height):
    print("a spruce!")
    i = 1
    j = height - i
    l = 1
    while l <= height:
        print(" " * j, sep="", end="")
        print("*" * i)
        i += 2 # Stars
        j -= 1 # Spaces
        l += 1 # Counter
    i = 1
    j = height - i
    print(" " * j, sep="", end="")
    print("*")
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)