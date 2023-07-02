# Write your solution here
def longest_series_of_neighbours(int_list: list):
    longest_series = 1
    current_series = 1

    for i in range(1, len(int_list)):
        if abs(int_list[i-1] - int_list[i]) == 1:
            current_series += 1
        else:
            current_series = 1
        longest_series = max(longest_series, current_series)

    return longest_series

if __name__ == "__main__":
    print(longest_series_of_neighbours([1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]))