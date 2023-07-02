# Write your solution here
def everything_reversed(str_list: list):
    reversed_list = []
    for word in str_list:
        reversed_list.append(word[::-1])
    return reversed_list[::-1]

if __name__ == "__main__":
    print(everything_reversed(["Ingen", "ko", "på", "isen"]))

