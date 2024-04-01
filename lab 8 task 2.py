from tkinter import *
from tkinter import messagebox

def create_tic_tac_toe_game(root, frame):
    board = [{1: " ", 2: " ", 3: " ",
             4: " ", 5: " ", 6: " ",
             7: " ", 8: " ", 9: " "},
            {10: " ", 11: " ", 12: " ",
             13: " ", 14: " ", 15: " ",
             16: " ", 17: " ", 18: " "},
            {19: " ", 20: " ", 21: " ",
             22: " ", 23: " ", 24: " ",
             25: " ", 26: " ", 27: " "}]

    turn = "X"
    game_end = False
    global count
    count = 0

    def updateBoard():
        for key in board.keys():
            buttons[key - 1]["text"] = board[key]

    def check_for_win(player):
        if (((board[1] == board[2] == board[3] == player) or
            (board[4] == board[5] == board[6] == player) or
            (board[7] == board[8] == board[9] == player) or
            (board[1] == board[4] == board[7] == player) or
            (board[2] == board[5] == board[8] == player) or
            (board[3] == board[6] == board[9] == player) or
            (board[1] == board[5] == board[9] == player) or
            (board[3] == board[5] == board[7] == player) or
            (board[10] == board[11] == board[12] == player) or
            (board[13] == board[14] == board[14] == player) or
            (board[16] == board[17] == board[18] == player) or
            (board[10] == board[13] == board[16] == player) or
            (board[11] == board[14] == board[17] == player) or
            (board[12] == board[14] == board[18] == player) or
            (board[10] == board[14] == board[18] == player) or
            (board[12] == board[14] == board[16] == player) or
            (board[19]) == board[20] == board[21] == player) or
            (board[22] == board[23] == board[24] == player) or
            (board[25] == board[26] == board[27] == player) or
            (board[19] == board[22] == board[25] == player) or
            (board[20] == board[23] == board[26] == player) or
            (board[21] == board[24] == board[27] == player) or
            (board[19] == board[23] == board[27] == player) or
            (board[21] == board[23] == board[25] == player) or
            (board[1] == board[11] == board[12] == player) or
            (board[1] == board[20] == board[21] == player) or
            (board[1] == board[11] == board[3] == player) or
            (board[1] == board[20] == board[3] == player) or
            (board[1] == board[2] == board[12] == player) or
            (board[1] == board[11] == board[21] == player) or
            (board[1] == board[2] == board[21] == player) or
            (board[1] == board[20] == board[12] == player) or
            (board[4] == board[14] == board[15] == player) or
            (board[4] == board[23] == board[24] == player) or
            (board[4] == board[15] == board[23] == player) or
            (board[4] == board[14] == board[24] == player) or
            (board[4] == board[23] == board[6] == player) or
            (board[4] == board[14] == board[6] == player) or
            (board[4] == board[5] == board[15] == player) or
            (board[4] == board[5] == board[24] == player) or
            (board[7] == board[17] == board[18] == player) or
            (board[7] == board[26] == board[27] == player) or
            (board[7] == board[17] == board[9] == player) or
            (board[7] == board[26] == board[9] == player) or
            (board[7] == board[8] == board[18] == player) or
            (board[7] == board[8] == board[27] == player) or
            (board[7] == board[17] == board[27] == player) or
            (board[7] == board[26] == board[18] == player) or
            (board[10] == board[2] == board[3] == player) or
            (board[10] == board[20] == board[21] == player) or
            (board[10] == board[11] == board[3] == player) or
            (board[10] == board[2] == board[12] == player) or
            (board[10] == board[20] == board[12] == player) or
            (board[10] == board[2] == board[21] == player) or
            (board[10] == board[20] == board[3] == player) or
            (board[10] == board[11] == board[21] == player) or
            (board[13] == board[5] == board[15] == player) or
            (board[13] == board[5] == board[6] == player) or
            (board[13] == board[5] == board[24] == player) or
            (board[13] == board[14] == board[6] == player) or
            (board[13] == board[14] == board[24] == player) or
            (board[13] == board[23] == board[24] == player) or
            (board[13] == board[23] == board[15] == player) or
            (board[13] == board[23] == board[6] == player) or
            (board[16] == board[8] == board[9] == player) or
            (board[16] == board[8] == board[18] == player) or
            (board[16] == board[8] == board[27] == player) or
            (board[16] == board[17] == board[9] == player) or
            (board[16] == board[17] == board[27] == player) or
            (board[16] == board[26] == board[27] == player) or
            (board[16] == board[26] == board[18] == player) or
            (board[16] == board[26] == board[9] == player) or
             (board[10] == board[2] == board[3] == player) or
             (board[10] == board[20] == board[21] == player) or
             (board[10] == board[11] == board[3] == player) or
             (board[10] == board[2] == board[12] == player) or
             (board[10] == board[20] == board[12] == player) or
             (board[10] == board[2] == board[21] == player) or
             (board[10] == board[20] == board[3] == player) or
             (board[10] == board[11] == board[21] == player) or
             (board[19] == board[20] == board[3] == player) or
             (board[19] == board[20] == board[12] == player) or
             (board[19] == board[2] == board[3] == player) or
             (board[19] == board[2] == board[12] == player) or
             (board[19] == board[2] == board[21] == player) or
             (board[19] == board[11] == board[12] == player) or
             (board[19] == board[11] == board[3] == player) or
             (board[19] == board[11] == board[21] == player) or
             (board[22] == board[23] == board[6] == player) or
             (board[22] == board[23] == board[15] == player) or
             (board[22] == board[5] == board[6] == player) or
             (board[22] == board[5] == board[15] == player) or
             (board[22] == board[5] == board[24] == player) or
             (board[22] == board[14] == board[6] == player) or
             (board[22] == board[14] == board[15] == player) or
             (board[22] == board[14] == board[24] == player) or
             (board[25] == board[26] == board[9] == player) or
             (board[25] == board[26] == board[18] == player) or
             (board[25] == board[8] == board[9] == player) or
             (board[25] == board[8] == board[18] == player) or
             (board[25] == board[8] == board[27] == player) or
             (board[25] == board[17] == board[9] == player) or
             (board[25] == board[17] == board[18] == player) or
             (board[25] == board[17] == board[27] == player)):
            return True

        return False

    def restartGame():
        global game_end
        game_end = False
        for button in buttons:
            button["text"] = " "

        for i in board.keys():
            board[i] = " "

        titleLabel = Label(frame1, text="Tic Tac Toe", font=("Bradley Hand ITC", 30), bg="pink", width=15)
        titleLabel.grid(row=0, column=0)

    def checkForDraw():
        return all(board[i] != " " for i in board.keys())

    def play(event):
        global turn, game_end, count
        if game_end:
            return

        button = event.widget
        buttonText = str(button)
        clicked = buttonText[-1]
        if clicked == "n":
            clicked = 1
        else:
            clicked = int(clicked)

        if button["text"] == " ":
            if turn == "x":
                button["text"] = "X"
                board[clicked] = turn
                count += 1
                if check_for_win(turn):
                    winningLabel = Label(frame1, text=f"{turn} wins the game", bg="pink", font=("Bradley Hand ITC", 26),
                                         width=16)
                    winningLabel.grid(row=0, column=0, columnspan=3)
                    game_end = True
                turn = "O"

            else:
                button["text"] = "O"
                board[clicked] = turn
                count += 1
                if check_for_win(turn):
                    winningLabel = Label(frame1, text=f"{turn} wins the game", bg="pink", font=("Bradley Hand ITC", 26),
                                         width=16)
                    winningLabel.grid(row=0, column=0, columnspan=3)
                    game_end = True
                turn = "x"

            if not game_end and checkForDraw():
                drawLabel = Label(frame1, text=f"Game Draw", bg="pink", font=("Bradley Hand ITC", 26), width=16)
                drawLabel.grid(row=0, column=0, columnspan=3)
                game_end = True

    # Tic Tac Toe Board
    buttons = []
    for i in range(3):
        for j in range(3):
            button = Button(frame, text=" ", width=4, height=2, font=("Bradley Hand ITC", 30), bg="grey", relief=RAISED,
                            borderwidth=5)
            button.grid(row=i, column=j)
            button.bind("<Button-1>", play)
            buttons.append(button)


    restart_button = Button(frame, text="Restart Game", width=19, height=1, font=("Bradley Hand ITC", 20), bg="Red", relief=RAISED, borderwidth=5, command=restartGame)
    restart_button.grid(row=3, column=0, columnspan=3)


root = Tk()
root.geometry("1500x1100")
root.title("Tic Tac Toe")
root.resizable(0, 0)


frame1 = Frame(root)
frame1.grid(row=0, column=0, padx=10)

frame2 = Frame(root)
frame2.grid(row=0, column=1, padx=10)

frame3 = Frame(root)
frame3.grid(row=0, column=2, padx=10)


create_tic_tac_toe_game(root, frame1)
create_tic_tac_toe_game(root, frame2)
create_tic_tac_toe_game(root, frame3)

root.mainloop()