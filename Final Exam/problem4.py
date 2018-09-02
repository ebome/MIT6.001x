'''
You are given the following definitions:
A run of monotonically increasing numbers means that a number at position k+1 in the sequence is greater than or equal to the number at
position k in the sequence.
A run of monotonically decreasing numbers means that a number at position k+1 in the sequence is less than or equal to the number at
position k in the sequence.
Implement a function that meets the specifications below.
'''
# For example:
# If L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2] then the longest run of monotonically increasing numbers in L is [3, 4, 5, 7, 7] and the longest
# run of monotonically decreasing numbers in L is [10, 4, 3]. Your function should return the value 26 because the longest run of
# monotonically increasing integers is longer than the longest run of monotonically decreasing numbers.
# If L = [5, 4, 10] then the longest run of monotonically increasing numbers in L is [4, 10] and the longest run of monotonically
# decreasing numbers in L is [5, 4]. Your function should return the value 9 because the longest run of monotonically decreasing integers
# occurs before the longest run of monotonically increasing numbers.

def longestRun(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    incrementCount = 0
    maxcount = 0
    result = 0

    for char in range(len(L) - 1):
        if (L[char+1] >= L[char]):
            incrementCount += 1            
            if incrementCount > maxcount:
                maxcount = incrementCount
                result = char + 1
        else:
            incrementCount = 0
        
    startposition = result - maxcount
    return sum(L[startposition:result + 1])
