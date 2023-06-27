# Write your solution here
list = [1, 2, 3, 4, 5]

while True:
    index = int(input("Index: "))
    if index == -1:
        break
    if index < 0 or index >= len(list):
        print("Invalid index")
        continue
    list[index] = int(input("New value: "))
    print(list)