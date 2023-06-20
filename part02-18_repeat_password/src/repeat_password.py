# Write your solution here
password = input("Password: ")
while True:
    password_two = input("Repeat password: ")

    if (password == password_two):
        break
    else:
        print("They do not match!")

print("User account created!")