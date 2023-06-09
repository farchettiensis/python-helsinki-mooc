# Write your solution here
total_students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))

num_groups = total_students // group_size 
remainder = total_students % group_size

if (remainder > 0):
    num_groups += 1

print(f"Number of groups formed: {num_groups}")