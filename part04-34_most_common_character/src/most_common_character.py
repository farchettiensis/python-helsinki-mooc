# Write your solution here
def most_common_character(string: str):
    max_count = 0
    most_common_char = ""

    for char in string:
        count = string.count(char)
        if count > max_count:
            max_count = count
            most_common_char = char

    print(max_count, end=": ")
    return most_common_char

if __name__ == "__main__":
    print(most_common_character("saippuakivikauppias"))
    print(most_common_character("Ingen ko på isen"))
