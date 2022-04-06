#!/usr/bin/env python

#IMPORT BLOCK(2022/04/06 -JW)
import random

#GLOBAL VARIABLES(2022/04/06 -JW)
secretNumLength = 3
maxNumberOfGuesses = 10
debug = False

#FUNCTION BLOCK(2022/04/06 -JW)
def preamble():
    print('''Bagels, a deductive logic game.
Created by Al Sweigart al@inventwithpython.com
Coded by John Weis https://github.com/weisje
I am thinking of a {}-digit number.  Try to guess what it is.
Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.

For example, if the secret number was 248 & your guess was 843, the clues would be Fermi Pico.
'''.format(secretNumLength))

def generateSecretNum():
    secretNumber = ''

    numList = list('0123456789')
    random.shuffle(numList)

    for digit in range(secretNumLength):
        secretNumber += str(numList[digit])
    return secretNumber

def generateClues(guess, secretNumber):
    clues = []
    if(guess == secretNumber):
        return "That's correct!"

    for digit in range(len(guess)):
        if guess[digit] == secretNumber[digit]:
            clues.append('Fermi')
        elif guess[digit] in secretNumber:
            clues.append('Pico')

    if(len(clues) == 0):
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)

def main():
    preamble()
    while True:
        secretNumber = generateSecretNum()
        guessCount = 1

        print('I have thought of a number.')
        print('You have {} guesses to get it.'.format(maxNumberOfGuesses))
        if(debug == True):
            #<DEBUG>: Prints secretNumber while coding to confirm it is being generated properly(2022/04/06 -JW)
            print(secretNumber)
            #</DEBUG>
        while guessCount <= maxNumberOfGuesses:
            guess = ''
            while len(guess) != secretNumLength or not guess.isdecimal():
                print("Guess #{}: ".format(guessCount))
                guess = input('> ')
            clues = generateClues(guess, secretNumber)
            print(clues)
            guessCount += 1

            if guess == secretNumber:
                break
            if guessCount > maxNumberOfGuesses:
                print('You ran out of guesses!\nThe answer was: {}'.format(secretNumber))
        print('Do you want to play again? (Y)es or (N)o')
        if not input('> ').upper().startswith('Y'):
            break
    print('Thanks for playing!')

if __name__ == '__main__':
    main()

# JOURNAL:
# This project is a direct one from Al Sweigart's "The Big Book of Small Python Projects." This is the first program listed from the book & I will attempt to program the project on my own from the description before comparing my code to Sweigart's.

#Project Link: https://inventwithpython.com/bigbookpython/project1.html
#Alt Link: https://web.archive.org/web/20211122185903/https://inventwithpython.com/bigbookpython/project1.html
#Author's Books: https://nostarch.com/search/al%20sweigart
#Author's Patreon: https://www.patreon.com/AlSweigart
#Author's Github: https://github.com/asweigart
