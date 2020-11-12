
"""
Hang man!
Rules are simple: 
    You have 8 Guesses
    You only lose a guess only if you are wrong
    If you accidentally guess the same letter twice wont count as a guess
Enjoy!
"""
import random

WORDLIST_FILENAME = "trump_nonsense.txt"

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

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    unique = len(list(set(secretWord)))
    found = []
    counter = 0
    for letter in lettersGuessed:
        if letter in secretWord and letter not in found:
            counter += 1 
            found.append(letter)
    if counter == unique :
        return True       
    return False

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    List = list(secretWord)
    for i in range(len(List)):
        if not List[i] in lettersGuessed:
          List[i] = "_ "
    return ''.join(List)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available = list("abcdefghijklmnopqrstuvwxyz")
    for char in lettersGuessed:
        available.pop(available.index(char))
    return ''.join(available)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.
    
    '''
    # Declare Gueeses and lettersGuessed
    guessNumber = 8
    lettersGuessed = []
    # Introduce the gamne
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + repr(len(secretWord)) + " letters long.")
    print("-------------")
    # Continue while players's guess > 0
    while guessNumber > 0:
    # Display guesses and Remaining letters
        print("You have " + repr(guessNumber) + " guesses left.")
        print("Available letters: " + getAvailableLetters(lettersGuessed), end='')
        # Ask for user input
        Guess = input(" || Please guess a letter: ")
        # Check guess against previous
        if Guess.lower() in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            print("-------------")
            continue
        # Append guess to lettersGuessed 
        else:
            lettersGuessed.append(Guess.lower())
        # check if guess is in the secret word!
            if Guess.lower() in secretWord:
                print("Good guess: " +getGuessedWord(secretWord,lettersGuessed))
                print("-------------")
            else:
                print("Oops! That letter is not in  word: " + getGuessedWord(secretWord,lettersGuessed))
                guessNumber = guessNumber - 1
                print("-------------")
        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations, you won!")
            break
        if guessNumber == 0:
            print("Sorry, you ran out of guesses. The word was " + secretWord)
            break
        
secretWord= chooseWord(wordlist).lower()
hangman(secretWord)
