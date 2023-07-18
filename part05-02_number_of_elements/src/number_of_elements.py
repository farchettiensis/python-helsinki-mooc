def count_matching_elements(my_matrix: list, element: int):
    matching_elements = 0
    for row in range(len(my_matrix)):
        for column in range(len(my_matrix[row])):
            if my_matrix[row][column] == element:
                matching_elements += 1
    return matching_elements

if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))
