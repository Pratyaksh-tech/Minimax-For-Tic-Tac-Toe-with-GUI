import tkinter as tk
from tkinter import messagebox

def spaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False

def reset():
	global myturn
	for key in board.keys():
		buttons[key]['text'] = '';
	for i in board:
		board[i] = ' '
	if myturn:
		compMove()
		myturn = False
	else:
		myturn = True

def insertLetter(letter, position):
    global searches
    if spaceIsFree(position):
        board[position] = letter
        updateGUI()

        if letter == bot:
            print(f"No. of moves Bot searches ahead are {searches}\n")

        if checkDraw():
            print("Draw!")
            messagebox.showinfo("Game Over", "It's a Draw!")
            reset();
            return

        if checkForWin():
            if letter == 'X':
                print("Bot wins!")
                messagebox.showinfo("Game Over", "Bot wins!")
            else:
                print("Player wins!")
                messagebox.showinfo("Game Over", "Player wins!")
            reset();
            return
    else:
        print("Can't insert there!")
        position = int(input("Please enter a new position:  "))
        insertLetter(letter, position)
        return

def checkForWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

def checkWhichMarkWon(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False

def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True

def compMove():
    bestScore = -800
    bestMove = 0
    for key in board.keys():
        if board[key] == ' ':
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key

    insertLetter(bot, bestMove)
    return

def minimax(board, depth, isMaximizing):
    global searches
    searches += 1;
    if checkWhichMarkWon(bot):
        return 1
    elif checkWhichMarkWon(player):
        return -1
    elif checkDraw():
        return 0

    if isMaximizing:
        bestScore = -800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = bot
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore

    else:
        bestScore = 800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if score < bestScore:
                    bestScore = score
        return bestScore

def updateGUI():
    for key in board.keys():
        buttons[key]['text'] = board[key]

def create_buttons(frame):
    buttons = {}
    for i in range(1, 10):
        buttons[i] = tk.Button(frame, text=' ', font=('Helvetica', 20), height=2, width=4,
                               command=lambda pos=i: playerMove(pos))
        buttons[i].grid(row=(i - 1) // 3, column=(i - 1) % 3)
    return buttons

def playerMove(position):
    global myturn
    if spaceIsFree(position):
       	insertLetter(player, position)
        compMove()
    else:
        messagebox.showerror("Invalid Move", "Can't insert there!")

board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

player = 'O'
bot = 'X'
global searches
searches = 0
global myturn
myturn = False

window = tk.Tk()
window.title("Tic Tac Toe")
title_label = tk.Label(window, text="Tic Tac Toe", font=("Helvetica", 24))
title_label.pack(pady=20)

buttons_frame = tk.Frame(window)
buttons_frame.pack()

buttons = create_buttons(buttons_frame)
compMove()
window.mainloop()
