# Hangman game
'''
Now you will implement the function hangman, which takes one parameter - the secretWord
the user is to guess. This starts up an interactive game of Hangman between the user and
the computer. Be sure you take advantage of the three helper functions, isWordGuessed, getGuessedWord,
and getAvailableLetters, that you've defined in the previous part.

Hints:

Consider using lower() to convert user input to lower case. For example:

>>guess = 'A'
>>guessInLowerCase = guess.lower()

Consider writing additional helper functions if you need them!

There are four important pieces of information you may wish to store:
secretWord: The word to guess.
lettersGuessed: The letters that have been guessed so far.
mistakesMade: The number of incorrect guesses made so far.
availableLetters: The letters that may still be guessed. Every time a player guesses
a letter, the guessed letter must be removed from availableLetters (and if they guess
a letter that is not in availableLetters, you should print a message telling them
they've already guessed that - so try again!).
'''
import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    guess = False
    for c in secretWord:
        if c in lettersGuessed:
            guess = True
            continue
        elif c not in lettersGuessed:
            guess = False
            break
    return guess


def getGuessedWord(secretWord, lettersGuessed):
    temp=[]
    for eachLetter in secretWord:
        if eachLetter in lettersGuessed:
            temp.append(eachLetter)
        else:
            temp.append('_ ')
    ans=''.join(temp)
    return ans


def getAvailableLetters(lettersGuessed):
    order=string.ascii_lowercase
    temp=[]
    for l in order:
        if l not in lettersGuessed:
            temp.append(l)
        elif l in lettersGuessed:
            continue
    ans=''.join(temp)
    return ans


def hangman(secretWord):
    print('Welcome to the game, Hangman!\nI am thinking of a word that is ',len(secretWord),' letters long.')

    mistakesMade=0
    availableLetters = string.ascii_lowercase # 26 letters
    lettersGuessed = []

    while 8-mistakesMade > 0:
        print('-------------')
        print('You have',8-mistakesMade,'guesses left.')
        print('Available letters:',availableLetters)
        userGuess = str(input('Please guess a letter:')).lower()
        if userGuess in lettersGuessed:
            print('Oops! You\'ve already guessed that letter:',getGuessedWord(secretWord, lettersGuessed) )
        if userGuess not in lettersGuessed:
            lettersGuessed.append(userGuess)
            if userGuess in secretWord:
                print('Good guess: ',getGuessedWord(secretWord, lettersGuessed) )
                availableLetters = getAvailableLetters(lettersGuessed) # returns a string
        if userGuess not in secretWord:
            lettersGuessed.append(userGuess)
            print('Oops! That letter is not in my word:',getGuessedWord(secretWord, lettersGuessed) )
            availableLetters = getAvailableLetters(lettersGuessed) # returns a string
            mistakesMade = mistakesMade+1


        if isWordGuessed(secretWord, lettersGuessed)==True: # ALL the letters of secretWord are in lettersGuessed
            print('------------\nCongratulations, you won!' )
            break

    if 8 - mistakesMade == 0:
        print('------------\nSorry, you ran out of guesses. The word was else.' )
