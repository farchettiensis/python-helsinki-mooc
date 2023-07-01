# Write your solution here
def even_numbers(num_list: list):
    even_list = []
    for i in num_list:
        if i % 2 == 0:
            even_list.append(i)
    return even_list

if __name__ == "__main__":
    print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))