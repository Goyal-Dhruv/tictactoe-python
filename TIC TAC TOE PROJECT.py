#!/usr/bin/env python
# coding: utf-8

# In[2]:


def sum(a, b, c):
    return a + b + c

# Reference board showing the indexes
def printReferenceBoard():
    print("Reference Board: (Indexes for input)")
    print(" 0 | 1 | 2 ")
    print("---|---|---")
    print(" 3 | 4 | 5 ")
    print("---|---|---")
    print(" 6 | 7 | 8 ")
    print("\n")

# Main game board showing the current state of the game
def printBoard(xState, zState):
    zero = 'X' if xState[0] else ('O' if zState[0] else ' ')
    one = 'X' if xState[1] else ('O' if zState[1] else ' ')
    two = 'X' if xState[2] else ('O' if zState[2] else ' ')
    three = 'X' if xState[3] else ('O' if zState[3] else ' ')
    four = 'X' if xState[4] else ('O' if zState[4] else ' ')
    five = 'X' if xState[5] else ('O' if zState[5] else ' ')
    six = 'X' if xState[6] else ('O' if zState[6] else ' ')
    seven = 'X' if xState[7] else ('O' if zState[7] else ' ')
    eight = 'X' if xState[8] else ('O' if zState[8] else ' ')
    
    # Print the main game board with current state
    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")

# Function to check for a win or draw
def checkWinOrDraw(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    
    # Check for winning condition
    for win in wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            print("X Won the match!")
            return 1
        if sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            print("O Won the match!")
            return 0
    
    # Check for a draw (if all positions are filled and no winner)
    if all(xState[i] == 1 or zState[i] == 1 for i in range(9)):
        print("The game is a draw!")
        return 2
    
    return -1

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1  # 1 for X and 0 for O
    print("Welcome to Tic Tac Toe\n")
    
    # Print the reference board before starting the game
    printReferenceBoard()
    
    while True:
        printBoard(xState, zState)
        if turn == 1:
            print("X's Chance")
            value = int(input("Please enter a value (0-8): "))
            if xState[value] == 0 and zState[value] == 0:
                xState[value] = 1
            else:
                print("Invalid move! Try again.")
                continue
        else:
            print("O's Chance")
            value = int(input("Please enter a value (0-8): "))
            if xState[value] == 0 and zState[value] == 0:
                zState[value] = 1
            else:
                print("Invalid move! Try again.")
                continue
        
        # Check if there is a win or draw
        result = checkWinOrDraw(xState, zState)
        if result != -1:
            printBoard(xState, zState)
            if result == 1:
                print("Congratulations, X wins!")
            elif result == 0:
                print("Congratulations, O wins!")
            elif result == 2:
                print("It's a draw!")
            print("Match over")
            break

        turn = 1 - turn  # Switch turn between X and O


# In[ ]:




