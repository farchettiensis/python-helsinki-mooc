# Write your solution here
string = input("Please type in a string: ")
i = -1
slice = ""

while i >= -len(string):
    #print(-len(string))
    #print(i)
    slice = string[i] + slice
    print(slice)
    i -= 1