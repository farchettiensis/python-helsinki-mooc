# Write your solution here
list = []
i = 1
print(f"The list is now {list}")

while True:
    operation = input("a(d)d, (r)emove or e(x)it: ")
    if operation == "d":
        list.append(i)
        print(f"The list is now {list}")
        i += 1
    elif operation == "r":
        list.pop()
        print(f"The list is now {list}")
        i -= 1
    elif operation == "x":
        print("Bye!")
        break
    else:
        print("Invalid option")
        continue
