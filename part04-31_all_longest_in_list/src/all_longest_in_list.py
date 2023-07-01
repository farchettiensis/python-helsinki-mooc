# Write your solution here
def all_the_longest(string_list: list):
    result = []
 
    for strings in string_list:
        if result == [] or len(strings) > len(result[0]):
            result = [strings]
        elif len(strings) == len(result[0]):
            result.append(strings)
    return result

if __name__ == "__main__":
    strings = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    print(all_the_longest(strings))
