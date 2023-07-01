# Write your solution here
def distinct_numbers(num_list: list):
    distinct_list = []
    for i in num_list:
        if i not in distinct_list:
            distinct_list.append(i)
    return sorted(distinct_list)

if __name__ == "__main__":
    print(distinct_numbers([3, 2, 2, 1, 3, 3, 1]))