# Write your solution here
def print_many_times(text, times):
    print((text + "\n") * times, end="")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print_many_times("python", 5)
    print_many_times("Java sucks", 3)