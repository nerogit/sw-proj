from hangman import Hangman
from guess import Guess
from word import Word


def gameMain():
    word = Word('words.txt')
    guess = Guess(word.randFromDB())

    finished = False
    hangman = Hangman()
    maxTries = hangman.getLife()

    while guess.numTries < maxTries:

        display = hangman.get(maxTries - guess.numTries)
        print(display)
        guess.display()

        guessedChar = input('Select a letter: ')
        if len(guessedChar) != 1:
            print('One character at a time!')
            continue
        if guessedChar in guess.guessedChars:
            print('You already guessed \"' + guessedChar + '\"')
            continue

        finished = guess.guess(guessedChar)
        if finished:
            break

    if finished:
        print('========== result ==========')
        print('Word:', guess.secretWord)
        print('Success')
    else:
        print(hangman.get(0))
        print('========== result ==========')
        print('word [ ' + guess.secretWord + ' ]')
        print('guess [ ' + guess.currentStatus + ']')
        print('Fail')


if __name__ == '__main__':
    gameMain()
