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
import emoji

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
    global phrase
    if gameMode == 0: #PvP
        phrase = (str(input(playerTwo + ", pick the phrase to be guessed: "))).upper()
        hint = input(playerTwo + ", give a hint: ")

        os.system('cls' if os.name == 'nt' else 'clear') # clear the terminal

        print("The hint is: " + hint)
    elif gameMode == 1: #PvCPU; to be implemented
        # open file
        # choose random int based on file line #
        # scan until line # reached
        # read line, parse by commas, save phrase and hint
        import random
        rawstr = random.choice(list(open('dict.txt')))
        rawstrsplit = rawstr.split(",")
        phrase = rawstrsplit[1].upper()
        print("The computer has chosen a phrase.")
        hint = rawstrsplit[0]
        print("The hint is: " + hint)
    else:
        print("ダメだね\nダメよ\nダメなのよ\n")
    
    print("Player 1, you may begin guessing.")

# initialize hiddenPhrase based on given phrase
def setHiddenPhrase():
    global hiddenPhrase
    hiddenPhrase = ""
    for letter in phrase:
        if letter == ' ':
            hiddenPhrase += ' '
        elif letter == '\'':
            hiddenPhrase += '\''
        elif letter != '\n':
            hiddenPhrase += '*'
    print(hiddenPhrase)

# already checked for validity of guess, checked if not already guessed
def updateHiddenPhrase(difficulty, guess):
    global chances
    if guess[0] in phrase:
        global hiddenPhrase
        tempHidden = ""
        for i in range(len(phrase)):
            # preserves spaces and apostrophes and guessed letters
            if hiddenPhrase[i] != '*':
                tempHidden += hiddenPhrase[i]
            elif phrase[i] == guess[0]:
                tempHidden += str(guess[0])
            else:
                tempHidden += "*"
        hiddenPhrase = tempHidden
    else:
        chances = chances - 1
    print(hiddenPhrase)
    draw(difficulty)
    print(str(chances) + " chances left.")


def checkWin():
    global playerOneWin
    global playerTwoWin
    if hiddenPhrase == phrase:
        playerOneWin = True
        print(playerOne + " wins!")
    elif chances == 0:
        playerTwoWin = True
        print(playerTwo + " wins!")


def processInput(difficulty):
    while not playerOneWin and not playerTwoWin:
        guess = (str(input("Guess a letter: "))).upper()
        global A
        global Z
        while not isinstance(guess, str) or len(guess) != 1 or ord(guess[0]) < A or ord(guess[0]) > Z or guess[0] not in letters:
            print("Not a valid input, or letter has been guessed. Here are the letters that have not yet been guessed: ")
            print(', '.join(letters))
            print("")
            guess = (str(input("Guess a letter: "))).upper()
        global phrase
        letters.remove(guess[0]) # removes a guessed letter
        updateHiddenPhrase(difficulty, guess)
        checkWin()


def handleEasy():
    global chances
    chances = 10
    processInput(0)

def handleMedium():
    global chances
    chances = 6
    processInput(1)

def handleHard():
    global chances
    chances = 1
    processInput(2)


def draw(difficulty):
    if difficulty == 0 and chances == 10:
        drawGallows()
    elif difficulty == 0 and chances == 9:
        drawEasy9()
    elif difficulty == 0 and chances == 8:
        drawEasy8()
    elif difficulty == 0 and chances == 7:
        drawEasy7()
    elif difficulty == 0 and chances == 6:
        drawEasy6()
    elif difficulty == 0 and chances == 5: 
        drawEasy5()
    elif difficulty == 0 and chances == 4:
        drawEasy4()
    elif difficulty == 0 and chances == 3:
        drawEasy3()
    elif difficulty == 0 and chances == 2:
        drawEasy2()
    elif difficulty == 0 and chances == 1:
        drawEasy1()
    elif difficulty == 0 and chances == 0:
        drawEasy0()
    elif difficulty == 1 and chances == 6:
        drawGallows()
    elif difficulty == 1 and chances == 5:
        drawMedium5()
    elif difficulty == 1 and chances == 4:
        drawMedium4()
    elif difficulty == 1 and chances == 3:
        drawMedium3()
    elif difficulty == 1 and chances == 2:
        drawMedium2()
    elif difficulty == 1 and chances == 1:
        drawMedium1()
    elif difficulty == 1 and chances == 0:
        drawMedium0()
    elif difficulty == 2 and chances == 1:
        drawGallows()
    elif difficulty == 2 and chances == 0:
        drawHard()

def drawGallows(): # initial board
    print("     _____  ")
    print("    |     | ")
    print("          | ")
    print("          | ")
    print("          | ")
    print("    --------")

def drawEasy9():
    print("     _____  ")
    print("    |     | ")
    print("  𓁹       | ")
    print("          | ")
    print("          | ")
    print("    --------")

def drawEasy8():
    print("     _____  ")
    print("    |     | ")
    print("  𓁹𓁹     | ")
    print("          | ")
    print("          | ")
    print("    --------")

def drawEasy7():
    print("     _____  ")
    print("    |     | ")
    print("  𓁹𓂏𓁹   | ")
    print("          | ")
    print("          | ")
    print("    --------")

def drawEasy6():
    print("     _____  ")
    print("    |     | ")
    print("  𓁹𓂏𓁹𓂈 | ")
    print("          | ")
    print("          | ")
    print("    --------")

def drawEasy5():
    print("     _____  ")
    print("    |     | ")
    print(" 𓂈𓁹𓂏𓁹𓂈 | ")
    print("          | ")
    print("          | ")
    print("    --------")

def drawEasy4():
    print("     _____  ")
    print("    |     | ")
    print(" 𓂈𓁹𓂏𓁹𓂈 | ")
    print("    👚    | ")
    print("          | ")
    print("    --------")

def drawEasy3():
    print("     _____  ")
    print("    |     | ")
    print(" 𓂈𓁹𓂏𓁹𓂈 | ")
    print("   💪👚    | ")
    print("          | ")
    print("    --------")

def drawEasy2():
    print("     _____  ")
    print("    |     | ")
    print(" 𓂈𓁹𓂏𓁹𓂈 | ")
    print("   💪👚👎  | ")
    print("          | ")
    print("    --------")

def drawEasy1():
    print("     _____  ")
    print("    |     | ")
    print(" 𓂈𓁹𓂏𓁹𓂈 | ")
    print("   💪👚👎  | ")
    print("   �     | ")
    print("    --------")

def drawEasy0():
    print("     _____  ")
    print("    |     | ")
    print(" 𓂈𓁹𓂏𓁹𓂈 | ")
    print("   💪👚👎  | ")
    print("   �𓂾  | ")
    print("    --------")

def drawMedium5():
    print("     _____  ")
    print("    |     | ")
    print("    O     | ")
    print("          | ")
    print("          | ")
    print("    --------")

def drawMedium4():
    print("     _____  ")
    print("    |     | ")
    print("    O     | ")
    print("    |     | ")
    print("          | ")
    print("    --------")

def drawMedium3():
    print("     _____  ")
    print("    |     | ")
    print("    O     | ")
    print("   ✌|     | ")
    print("          | ")
    print("    --------")

def drawMedium2():
    print("     _____  ")
    print("    |     | ")
    print("    O     | ")
    print("   ✌|✌   | ")
    print("          | ")
    print("    --------")

def drawMedium1():
    print("     _____  ")
    print("    |     | ")
    print("    O     | ")
    print("   ✌|✌   | ")
    print("   /      | ")
    print("    --------")

def drawMedium0():
    print("     _____  ")
    print("    |     | ")
    print("    O     | ")
    print("   ✌|✌   | ")
    print("   / \    | ")
    print("    --------")

def drawHard():
    print("     _____  ")
    print("    |     | ")
    print("    O     | ")
    print("   /|\    | ")
    print("   / \    | ")
    print("    --------")


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