# Write your solution here
def list_sum(list1: list, list2: list):
    sum_list = []
    for i in list1:
        sum_list.append(i + list2[0])
        list2.pop(0)
    return sum_list

if __name__ == "__main__":
    list1 = [1, 2, 3]
    list2 = [7, 8, 9]
    print(list_sum(list1, list2))

""" Model solution:
def list_sum(list1: list, list2: list):
    results = []
    for i in range(len(list1)):
        results.append(list1[i] + list2[i])
 
    return results
"""

""" Using zip function:
def list_sum(list1: list, list2: list):
    results = []
    for item1, item2 in zip(list1, list2):
        results.append(item1 + item2)
    return results
"""