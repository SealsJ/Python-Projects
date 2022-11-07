#import random so AI picks random word, import list of words from words.py found on stack overflow
import random
from words import words
import string

def getWord(words):
    word = random.choice(words) #takes in list and randomly chooses word
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = getWord(words)
    wordLetters = set(word) #track letters in words
    alphabet = set(string.ascii_uppercase)
    usedLetters = set() #track the letters user has input

    lives = 7

    #getting a user to input their guess letter
    while len(wordLetters) > 0 and lives > 0:
        #letters used
        print('You have', lives, 'lives left and used these letters: ', ' '.join(usedLetters))

        #what the current word is based on letters guessed
        wordList = [letter if letter in usedLetters else '-' for letter in word]
        print('Current Word: ', ' '.join(wordList))


        userGuess = input("Guess a Letter: ").upper()
        if userGuess in alphabet - usedLetters:
            usedLetters.add(userGuess)
            if userGuess in wordLetters:
                wordLetters.remove(userGuess)
                print('')

            else:
                lives = lives - 1 #taking away 1 life if wrong guess
                print('\nYour Letter,', userGuess, 'is not in the word.')

        elif userGuess in usedLetters:
            print('\nYou have already used that character. Try a different letter!')

        else:
            print('\nInvalid character. Please try a different letter!')

    #Gers here when length of the word = 0 or lives = 0
    if lives == 0:
        print('Sorry you have ran out of guesses! The word was', word)
    else:
        print('Congrats! You got the word,', word, '!')

if __name__== '__main__':
    hangman()