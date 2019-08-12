# Hangman game


import random

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open('words.txt', 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)




def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True
    



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            result += letter
        else:
            result += '_ '
    return result



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    available = ''
    for letter in alphabet:
        if letter not in lettersGuessed:
            available += letter
    return available



def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is',len(secretWord),'letters long.')
    print('-------------')
    chancesLeft=8
    lettersGuessed=[]
    while chancesLeft>=1:
        print('You have',chancesLeft,'guesses left.')
        availableLetters=getAvailableLetters(lettersGuessed)
        print('Available letters:',availableLetters)
        char=input('Please guess a letter:')
        
        if char in availableLetters:
            lettersGuessed.append(char)
            if char in secretWord:
                print('Good guess:',getGuessedWord(secretWord, lettersGuessed))
                print('-------------')
                if isWordGuessed(secretWord, lettersGuessed)==True:
                    print('Congratulations, you won!')
                    return
                else:
                    continue
            else:
                print('Oops! That letter is not in my word:',getGuessedWord(secretWord, lettersGuessed))
                print('-------------')
            
        else:
            print('Oops! You\'ve already guessed that letter:',getGuessedWord(secretWord, lettersGuessed))
            print('-------------')
            continue
        chancesLeft-=1
        
    print('Sorry, you ran out of guesses. The word was',secretWord)





# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

