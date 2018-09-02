"""
You are given a dictionary aDict that maps integer keys to integer values.
Write a Python function that returns a list of keys in aDict that map to
dictionary values that appear exactly once in aDict.
This function takes in a dictionary and returns a list.
Return the list of keys in increasing order.
If aDict does not contain any values appearing exactly once, return an empty list.
If aDict is empty, return an empty list.
Hint: You may want to create another dictionary as an intermediate data structure.
For example:
If aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0} then your function should return [1, 3, 8]
If aDict = {1: 1, 2: 1, 3: 1} then your function should return []
"""

# Sample values for aDict

# Program should return [1,3, 8]
# aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}

# Program should return []
# aDict = {1: 1, 2: 1, 3: 1}


def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''

    # This removes all the dictionary values that are the same. 
    # Stores the remaining keys and values in a dictionary
    newDict = {k:v for k,v in aDict.items() if aDict.values().count(v)==1}
    # takes each key and stores it in a list called dict_list
    dict_list = []
    for key in newDict.keys():
        if key not in dict_list:
            dict_list.append(key)
    dict_list.sort()
    return dict_list
