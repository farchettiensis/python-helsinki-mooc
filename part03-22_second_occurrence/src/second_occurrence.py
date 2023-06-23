# Write your solution here
string = input("Please type in a string: ")
substr = input("Please type in a substring: ")
start_index = string.find(substr)
second_index = 0

if start_index != -1: 
    second_index = string.find(substr, start_index + len(substr))
    if second_index != -1:
        print(f"The second occurrence of the substring is at index {second_index}.")
    else:
        print("The substring does not occur twice in the string.")
else:
    print("The substring does not occur twice in the string.")