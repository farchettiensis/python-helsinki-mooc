# Write your solution here
def squared(text, num):
    chars = list(text)
    
    char_index = 0
    
    row = 0
    while row < num:
        col = 0
        while col < num:
            current_char = chars[char_index % len(chars)]
            print(current_char, end="")
            
            char_index += 1
            col += 1
        
        row += 1
        print()
        
# Testing the function
if __name__ == "__main__":
    squared("text", 3)

""" Model solution:
def squared(characters, size):
    i = 0
    row = ""
    while i < size * size:
        if i > 0 and i % size == 0:
            print(row)
            row = ""
        row += characters[i % len(characters)]
        i += 1
    print(row)
"""