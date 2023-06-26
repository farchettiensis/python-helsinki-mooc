# Write your solution here
def same_chars(string, num1, num2):
    if num1 > len(string) - 1 or num2 > len(string) - 1:
        return False
    elif string[num1] == string[num2]:
        return True
    else:
        return False
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
    print(same_chars("programmer", 6, 7)) 
    print(same_chars("programmer", 0, 12)) 