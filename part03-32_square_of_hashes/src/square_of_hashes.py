# Write your solution here
def hash_square(length):
    i = 1
    while length >= i:
        print("#"*length)
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)
    hash_square(3)