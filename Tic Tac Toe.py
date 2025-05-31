import tkinter as tk
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x500")
root.title("Tic Tac Toe")
root.configure(bg="#2E4053")  # Set a nice background color
frame1 = Frame(root, bg="#1F618D")
frame1.pack()
titlelabel = Label(frame1, text="Tic Tac Toe", font=("Arial", 30, 'bold'), bg="#1F618D", fg="white")
titlelabel.pack()

board = {1: " ", 2: " ", 3: " ",
         4: " ", 5: " ", 6: " ",
         7: " ", 8: " ", 9: " "}

turn = 'X'
winningLabel = None


def checkforwin(turn):
    # checking rows
    if board[1] == board[2] and board[2] == board[3] and board[3] == turn:
        return True

    elif board[4] == board[5] and board[5] == board[6] and board[6] == turn:
        return True

    elif board[7] == board[8] and board[8] == board[9] and board[9] == turn:
        return True

    # checking diagonal
    elif board[1] == board[5] and board[5] == board[9] and board[9] == turn:
        return True

    elif board[3] == board[5] and board[5] == board[7] and board[7] == turn:
        return True

    # checking column
    elif board[1] == board[4] and board[4] == board[7] and board[7] == turn:
        return True

    elif board[2] == board[5] and board[5] == board[8] and board[8] == turn:
        return True

    elif board[3] == board[6] and board[6] == board[9] and board[9] == turn:
        return True


def checkfordraw():
    for i in board.keys():
        if board[i] == " ":
            return False
    return True


def restartGame():
    global winningLabel, gameOver
    for button in Buttons:
        button['text'] = " "

    for i in board.keys():
        board[i] = ' '

    if winningLabel:
        winningLabel.destroy()
        winningLabel = None
    gameOver = False


gameOver = False


def play(event):
    global turn, winningLabel, gameOver
    if gameOver:
        return
    button = event.widget
    buttonText = str(button)
    clicked = buttonText[-1]
    if clicked == 'n':
        clicked = 1
    else:
        clicked = int(clicked)

    if button["text"] == " ":
        if turn == "X":
            button["text"] = 'X'
            board[clicked] = turn
            if checkforwin(turn):
                winningLabel = Label(frame2, text=f"{turn} wins the game", bg="Green", font=("Arial", 35))
                winningLabel.grid(row=4, column=0, columnspan=3)
                gameOver = True
            turn = "O"

        else:
            button["text"] = 'O'
            board[clicked] = turn
            if checkforwin(turn):
                winningLabel = Label(frame2, text=f"{turn} wins the game", bg="#1ABC9C", font=("Arial", 35))
                winningLabel.grid(row=4, column=0, columnspan=3)
                gameOver = True
            turn = 'X'

        if checkfordraw():
            winningLabel = Label(frame2, text=f"Game draw", bg="#1ABC9C", font=("Arial", 35))
            winningLabel.grid(row=4, column=0, columnspan=3)


# Tic Tac Toe Board
frame2 = Frame(root, bg="#2E4053")
frame2.pack()
# first Row
button1 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg="#F7DC6F", activebackground="#F1C40F",
                 relief=RAISED, borderwidth=5)
button1.grid(row=0, column=0, padx=5, pady=5)
button1.bind("<Button-1>", play)

button2 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg="#F7DC6F", activebackground="#F1C40F",
                 relief=RAISED, borderwidth=5)
button2.grid(row=0, column=1, padx=5, pady=5)
button2.bind("<Button-1>", play)

button3 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg="#F7DC6F", activebackground="#F1C40F",
                 relief=RAISED, borderwidth=5)
button3.grid(row=0, column=2, padx=5, pady=5)
button3.bind("<Button-1>", play)

# second Row
button4 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg="#F7DC6F", activebackground="#F1C40F",
                 relief=RAISED, borderwidth=5)
button4.grid(row=1, column=0, padx=10, pady=5)
button4.bind("<Button-1>", play)

button5 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg="#F7DC6F", activebackground="#F1C40F",
                 relief=RAISED, borderwidth=5)
button5.grid(row=1, column=1, padx=5, pady=5)
button5.bind("<Button-1>", play)

button6 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg="#F7DC6F", activebackground="#F1C40F",
                 relief=RAISED, borderwidth=5)
button6.grid(row=1, column=2, padx=5, pady=5)
button6.bind("<Button-1>", play)

# third Row
button7 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg="#F7DC6F", activebackground="#F1C40F",
                 relief=RAISED, borderwidth=5)
button7.grid(row=2, column=0, padx=5, pady=5)
button7.bind("<Button-1>", play)

button8 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg="#F7DC6F", activebackground="#F1C40F",
                 relief=RAISED, borderwidth=5)
button8.grid(row=2, column=1, padx=5, pady=5)
button8.bind("<Button-1>", play)

button9 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg="#F7DC6F", activebackground="#F1C40F",
                 relief=RAISED, borderwidth=5)
button9.grid(row=2, column=2, padx=5, pady=5)
button9.bind("<Button-1>", play)

restartButton = Button(frame2, text="Reset", width=12, height=1, font=("Arial", 20, "bold"), bg="#5DADE2", fg="black",
                       activebackground="#3498DB", relief=RAISED, borderwidth=2, command=restartGame)
restartButton.grid(row=3, column=0, columnspan=3, pady=5)

Buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

root.mainloop()