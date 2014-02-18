# Write a function that takes an iterable (something you can loop through, 
#   ie: string, list, or tuple) and produces a dictionary with all distinct 
#   elements as the keys, and the number of each element as the value

def count_unique(some_iterable):
    dictionary = {}

    for item in some_iterable:
        if item in dictionary.keys():
            dictionary[item] += 1
        else: 
            dictionary[item] = 1

    return dictionary

"""
Another way: 

def count_unique(some_iterable):
    dictionary = {}

    for i in range(len(some_iterable)):
        if not dictionary.get(some_iterable[i]):
            dictionary[some_iterable[i]] = 1
        elif dictionary.get(some_iterable[i]): 
            dictionary[some_iterable[i]] += 1

    return dictionary
"""



# Given two lists, (without using the keyword 'in' or the method 'index') return a list of all common items shared between both lists
def common_items(list1, list2):
    return []




# Given two lists, (without using the keyword 'in' or the method 'index') return a list of all common items shared between both lists. This time, use a dictionary as part of your solution.
def common_items2(list1, list2):
    return []

