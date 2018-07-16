'''
Implement the function getGuessedWord that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. 
This function returns a string that is comprised of letters and underscores, based on what letters in lettersGuessed are in secretWord. 
This shouldn't be too different from isWordGuessed!

Example Usage:

>>> secretWord = 'apple' 
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(getGuessedWord(secretWord, lettersGuessed))
'_ pp_ e'

When inserting underscores into your string, it's a good idea to add at least a space after each one, so it's clear to the user 
how many unguessed letters are left in the string (compare the readability of ____ with _ _ _ _ ). This is called usability

For this function, you may assume that all the letters in secretWord and lettersGuessed are lowercase.
'''
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    
    lettersGuessed: list, what letters have been guessed so far
    
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # Assume all the letters in secretWord and lettersGuessed are LOWERCASE
    temp=[]
    for eachLetter in secretWord:
        if eachLetter in lettersGuessed:
            temp.append(eachLetter)
        else:
            temp.append('_ ')
    ans=''.join(temp)
    return ans
