
i = input("Enter cells: ")
i = i.replace("_", " ")
i = list(i)

board = [
    [i[0], i[1], i[2]],
    [i[3], i[4], i[5]],
    [i[6], i[7], i[8]],
]

def board_display():
    print("---------")
    print("|", board[0][0],  board[0][1], board[0][2], "|")
    print("|", board[1][0],  board[1][1], board[1][2], "|")
    print("|", board[2][0],  board[2][1], board[2][2], "|")
    print("---------")

board_display()

while True:
    move = input("Enter the coordinates: ")
    x, y = move.split(" ")
    if x.isalpha() or y.isalpha():
        print("You should enter numbers!")
    elif int(x) < 1 or int(x) > 3 or int(y) < 1 or int(y) > 3:
        print("Coordinates should be from 1 to 3!")

    elif board[int(x) - 1][int(y) - 1] == "X" or board[int(x) - 1][int(y) - 1] == "O":
        print("This cell is occupied! Choose another one!")
    else:
        if int(x) == 1 and int(y) == 1:
            board[0][0] = "X"
        if int(x) == 1 and int(y) == 2:
            board[0][1] = "X"
        if int(x) == 1 and int(y) == 3:
            board[0][2] = "X"
        if int(x) == 2 and int(y) == 1:
            board[1][0] = "X"
        if int(x) == 2 and int(y) == 2:
            board[1][1] = "X"
        if int(x) == 2 and int(y) == 3:
            board[1][2] = "X"
        if int(x) == 3 and int(y) == 1:
            board[2][0] = "X"
        if int(x) == 3 and int(y) == 2:
            board[2][1] = "X"
        if int(x) == 3 and int(y) == 3:
            board[2][2] = "X"
        break

board_display()     


