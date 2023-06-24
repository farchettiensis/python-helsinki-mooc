# Write your solution here
editor = ""

while True:
    editor = input("Editor: ").lower()
    if editor == "word":
        print("awful")
    elif editor == "visual studio code":
        print("an excellent choice!")
        break
    else: 
        print("not good")