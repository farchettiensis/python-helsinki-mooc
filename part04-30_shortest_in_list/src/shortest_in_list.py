# Write your solution here
def shortest(string_list: list):
    result = ""
 
    for shortest in string_list:
        if result == "" or len(shortest) < len(result):
            result = shortest
    return result

""" Alternative solution:
def shortest(string_list: list):
    shortest_str = min(string_list, key=len)
    return shortest_str
"""
