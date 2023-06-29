# Write your solution here
def sum_of_positives(my_list):
    sum = 0
    for i in my_list:
        if i > 0:
            sum += i
    return sum

if __name__ == "__main__":
    sum_of_positives([1, -2, 3, -4, 5])
    sum_of_positives([1, 2, 3, 4, 5])
    sum_of_positives([1, 2])