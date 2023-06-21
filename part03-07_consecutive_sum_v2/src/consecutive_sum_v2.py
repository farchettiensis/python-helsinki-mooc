# Write your solution here
limit = int(input("Limit: "))
sum = 0
i = 1
string = "The consecutive sum: "

while sum < limit:
    string += str(i)
    sum += i
    i += 1

    if sum < limit:
        string += " + "

string += f" = {sum}"

print(string)


