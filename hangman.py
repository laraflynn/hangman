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


gameMode = -1
playerOne = "DEFAULT 1"
playerTwo = "DEFAULT 2"
phrase = ""
chances = -1


def getPlayerNames():
    global playerOne = input("Player 1's name: ")
    if gameMode == 0:
        global playerTwo = input("Player 2's name: ")
    else:
        global playerTwo = "CPU"
    

def getPhrase():
    if gameMode == 0: #PvP
        global phrase = input(playerTwo + ", pick the phrase to be guessed: ")
        hint = input(playerTwo + ", give a hint: ")

        os.system('cls' if os.name == 'nt' else 'clear')

        print("The hint is: " + hint)
    elif gameMode == 1: #PvCPU; to be implemented
        print("The computer has chosen a phrase.")
        print("The category is: ")
    else:
        print("ダメだね\nダメよ\nダメなのよ\n")
    
    print("Player 1, you may begin guessing.")



def handleEasy():
    global chances = 10


def handleMedium():
    global chances = 6


def handleHard():
    global chances = 1

def drawGallows(): # initial board
    print("     _____  ")
    print("    |     | ")
    print("          | ")
    print("          | ")
    print("          | ")
    print("    --------")

def drawHard():



if __name__ == '__main__':  
    # ask game mode
    inputText = input("Pick a game mode, 0 for PvP, 1 for PvCPU: ")
    while not isinstance(inputText, int) or (inputText != 0 and inputText != 1):
        inputText = input("Not a valid input. Pick a game mode: ")
    global gameMode = inputText

    # ask for difficulty
    difficulty = input("Pick a game mode, 0 for easy, 1 for medium, 2 for hard: ")
    while not isinstance(difficulty, int) or (difficulty != 0 and difficulty != 1 and difficulty != 2):
        difficulty = input("Not a valid input. Pick a difficulty: ")
    
    # get the phrase and hint
    getPhrase()
    drawGallows()
    
    if difficulty == 0:
        handleEasy()
    elif difficulty == 1:
        handleMedium()
    else:
        handleHard()