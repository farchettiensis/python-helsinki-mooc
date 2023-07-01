# Write your solution here
def length_of_longest(string_list: list):
    result = ""
    for i in range(len(string_list)):
        if len(string_list[i]) > len(result):
            result = string_list[i]
    return len(result)

if __name__ == "__main__":
    print(length_of_longest(["saippuakivikauppias", "paholainen", "jordgubbe", "Ingen ko på isen"]))