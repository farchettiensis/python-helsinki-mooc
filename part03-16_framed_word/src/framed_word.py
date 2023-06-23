# Write your solution here
word = input("Word: ")
lspaces = ((28 - len(word)) // (2))
def left_spaces():
    if lspaces % 2 == 0:
        return (lspaces - 1) * ' '
    else:
        return (lspaces) * ' '
rspaces = (28 - ((28 - len(word)) // (2)) - len(word)) * ' '
 
print("*" * 30)
print(f"*{left_spaces()}{word}{rspaces}*")
print("*" * 30)







