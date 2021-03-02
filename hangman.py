# Hangman
# start: 2/25/2021

# player vs player
# ask players for name
# ask players for difficulty level
# ask player 2 for phrase and hint
# ask player 1 for guess every round
# if correct, fill in letters
# if incorrect, draw hangman figure
# if last figure was drawn then end game

# PvP: ask player 2 for phrase
# PvCPU: computer comes up with phrase
# gameplay in middle is the same
# PvP: if player 2 wins, print player 2 name
# PvCPU: if computer wins, print "Computer wins"

# used to clear terminal after player 2 inputs phrase
import os

A = 65
Z = 90
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

gameMode = -1
playerOne = "DEFAULT 1"
playerTwo = "DEFAULT 2"
phrase = "DEFAULT PHRASE"
hiddenPhrase = "DEFAULT HIDDEN PHRASE"
chances = -1
playerOneWin = False
playerTwoWin = False


def setPlayerNames():
    global playerOne
    playerOne = input("Player 1's name: ")
    global playerTwo
    if gameMode == 0:
        playerTwo = input("Player 2's name: ")
    else:
        playerTwo = "CPU"
    

def setPhrase():
    if gameMode == 0: #PvP
        global phrase
        phrase = input(playerTwo + ", pick the phrase to be guessed: ")
        hint = input(playerTwo + ", give a hint: ")

        os.system('cls' if os.name == 'nt' else 'clear') # clear the terminal

        print("The hint is: " + hint)
    elif gameMode == 1: #PvCPU; to be implemented
        print("The computer has chosen a phrase.")
        print("The category is: ")
    else:
        print("ダメだね\nダメよ\nダメなのよ\n")
    
    print("Player 1, you may begin guessing.")

# initialize hiddenPhrase based on given phrase
def setHiddenPhrase():
    global hiddenPhrase
    for letter in phrase:
        if letter == ' ':
            hiddenPhrase += ' '
        else:
            hiddenPhrase += '*'

# already checked for validity of guess, checked if not already guessed
def updateHiddenPhrase(guess):
    if guess[0] in phrase:
        global hiddenPhrase
        tempHidden = ""
        for i in range(len(phrase)):
            if hiddenPhrase[i] != '*': # preserves spaces and guessed letters
                tempHidden[i] = hiddenPhrase[i]
            elif phrase[i] == guess[0]:
                tempHidden[i] = guess[0]
            else:
                tempHidden[i] = '*'
        hiddenPhrase = tempHidden
    else:
        global chances
        chances = chances - 1

def checkWin():
    global playerOneWin
    global playerTwoWin
    if hiddenPhrase == phrase:
        playerOneWin = True
    elif chances == 0:
        playerTwoWin = True


def handleEasy():
    global chances
    chances = 10


def handleMedium():
    global chances
    chances = 6


def handleHard():
    global chances
    chances = 1
    
    while not playerOneWin and not playerTwoWin:
        guess = (str(input("Guess a letter: "))).upper()
        while not isinstance(guess, str) or len(guess) != 1 or guess[0] < A or guess[0] > Z:
            guess = (str(input("Not a valid input. Guess a letter: "))).upper()
            if guess[0] not in letters:
                print("This letter has already guessed.")
                print("These letters have not been guessed yet: ")
                guess = (str(input("Already guessed. Guess a letter: "))).upper()
        global phrase
        letters.remove(guess[0]) # removes a guessed letter
        updateHiddenPhrase(guess)
        checkWin()


def drawGallows(): # initial board
    print("     _____  ")
    print("    |     | ")
    print("          | ")
    print("          | ")
    print("          | ")
    print("    --------")

def drawHard():
    print("hard drawing")


if __name__ == '__main__':  
    # ask game mode
    inputText = int(input("Pick a game mode, 0 for PvP, 1 for PvCPU: "))
    while not isinstance(inputText, int) or (inputText != 0 and inputText != 1):
        inputText = input("Not a valid input. Pick a game mode: ")
    #global gameMode
    gameMode = inputText

    setPlayerNames()

    # ask for difficulty
    difficulty = int(input("Pick a game mode, 0 for easy, 1 for medium, 2 for hard: "))
    while not isinstance(difficulty, int) or (difficulty != 0 and difficulty != 1 and difficulty != 2):
        difficulty = input("Not a valid input. Pick a difficulty: ")
    
    # set the phrase, hidden phrase, and hint
    setPhrase()
    setHiddenPhrase()
    drawGallows()
    
    if difficulty == 0:
        handleEasy()
    elif difficulty == 1:
        handleMedium()
    else:
        handleHard()