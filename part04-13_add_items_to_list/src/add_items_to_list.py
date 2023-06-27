# Write your solution here
i = int(input("How many items: "))
j = 1
list = []

while i >= j:
    new_item = int(input(f"Item {j}: "))
    list.append(new_item)
    j += 1
print(list)