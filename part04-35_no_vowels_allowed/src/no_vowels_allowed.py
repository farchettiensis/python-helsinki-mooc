# Write your solution here
def no_vowels(string: str):
    vowels = "aeiou"
    result = ""

    for char in string:
        if char not in vowels:
            result += char

    return result

if __name__ == "__main__":
    print(no_vowels("saippuakivikauppias"))
    print(no_vowels("jordgubbe"))