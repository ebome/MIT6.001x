'''
Implement the function getAvailableLetters that takes in one parameter - a list of letters, lettersGuessed. 
This function returns a string that is comprised of lowercase English letters - all lowercase English letters that 
are not in lettersGuessed.

Example Usage:

>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(getAvailableLetters(lettersGuessed))
abcdfghjlmnoqtuvwxyz
Note that this function should return the letters in alphabetical order, as in the example above.

For this function, you may assume that all the letters in lettersGuessed are lowercase.
'''
import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    order=string.ascii_lowercase  # A string comprised of all lowercase letters
    
    temp=[]  # Work with strings as lists; turn them into strings only when needed
    for l in order:
        if l not in lettersGuessed:
            temp.append(l)
        elif l in lettersGuessed:
            continue
    
    ans=''.join(temp)
    return ans
