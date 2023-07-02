# Write your solution here
def formatted(float_list: list):
    formatted_strings = []
    for i in float_list:
        formatted_strings.append(f"{i:.2f}")
    return formatted_strings

if __name__ == "__main__":
    print(formatted([1.234567, 2.345678, 3.456789]))

