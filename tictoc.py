i = [' '] * 9

CHAR_X = "X"
CHAR_O = "O"
current_turn = CHAR_O

board = [
    [i[0], i[1], i[2]],
    [i[3], i[4], i[5]],
    [i[6], i[7], i[8]],
]

def board_display():
    print("---------")
    print("|", i[0],  i[1], i[2], "|")
    print("|", i[3],  i[4], i[5], "|")
    print("|", i[6],  i[7], i[8], "|")
    print("---------")

def x():
    if (i[0] == "X" and i[1] == "X" and i[2] == "X" or
        i[3] == "X" and i[4] == "X" and i[5] == "X" or
        i[6] == "X" and i[7] == "X" and i[8] == "X" or
        i[0] == "X" and i[3] == "X" and i[6] == "X" or
        i[1] == "X" and i[4] == "X" and i[7] == "X" or
        i[2] == "X" and i[5] == "X" and i[8] == "X" or
        i[0] == "X" and i[4] == "X" and i[8] == "X" or
        i[2] == "X" and i[4] == "X" and i[6] == "X"):
        print("X wins")
        return True
    else:
        return False

def o():
    if (i[0] == "O" and i[1] == "O" and i[2] == "O" or
        i[3] == "O" and i[4] == "O" and i[5] == "O" or
        i[6] == "O" and i[7] == "O" and i[8] == "O" or
        i[0] == "O" and i[3] == "O" and i[6] == "O" or
        i[1] == "O" and i[4] == "O" and i[7] == "O" or
        i[2] == "O" and i[5] == "O" and i[8] == "O" or
        i[0] == "O" and i[4] == "O" and i[8] == "O" or
        i[2] == "O" and i[4] == "O" and i[6] == "O"):
        print("O wins")
        return True
    else:
        return False

def imp():
    if i.count("X") - i.count("O") >= 2 or i.count("O") - i.count("X") >= 2:
        print("Impossible")
        return True
    else:
        return False

def blanks():
    if (i[0] == " " or i[1] == " " or i[2] == " " or 
        i[3] == " " or i[4] == " " or i[5] == " " or 
        i[6] == " " or i[7] == " " or i[8] == " "):
        return True
    else:
        return False

def blanks_result():
    if blanks() == False:
        print("Draw")
        return True
    else:
        return False

def handle_turn():
    move = input("Enter the coordinates: ")
    x, y = move.split(" ")

    if x.isalpha() or y.isalpha():
        print("You should enter numbers!")
        handle_turn()
    elif int(x) < 1 or int(x) > 3 or int(y) < 1 or int(y) > 3:
        print("Coordinates should be from 1 to 3!")
        handle_turn()
    else:
        if int(x) == 1 and int(y) == 1:
            if i[0] == " ":
                i[0] = current_turn
            else:
                print("This cell is occupied! Choose another one!")
                handle_turn()
        elif int(x) == 1 and int(y) == 2:
            if i[1] == " ":
                i[1] = current_turn
            else:
                print("This cell is occupied! Choose another one!")
                handle_turn()
        elif int(x) == 1 and int(y) == 3:
            if i[2] == " ":
                i[2] = current_turn
            else:
                print("This cell is occupied! Choose another one!")
                handle_turn()
        elif int(x) == 2 and int(y) == 1:
            if i[3] == " ":
                i[3] = current_turn
            else:
                print("This cell is occupied! Choose another one!")
                handle_turn()
        elif int(x) == 2 and int(y) == 2:
            if i[4] == " ":
                i[4] = current_turn
            else:
                print("This cell is occupied! Choose another one!")
                handle_turn()
        elif int(x) == 2 and int(y) == 3:
            if i[5] == " ":
                i[5] = current_turn
            else:
                print("This cell is occupied! Choose another one!")
                handle_turn()
        elif int(x) == 3 and int(y) == 1:
            if i[6] == " ":
                i[6] = current_turn
            else:
                print("This cell is occupied! Choose another one!")
                handle_turn()
        elif int(x) == 3 and int(y) == 2:
            if i[7] == " ":
                i[7] = current_turn
            else:
                print("This cell is occupied! Choose another one!")
                handle_turn()
        elif int(x) == 3 and int(y) == 3:
            if i[8] == " ":
                i[8] = current_turn
            else:
                print("This cell is occupied! Choose another one!")
                handle_turn()
    return
    
def win_check():
    global gameplay
    if x() or o() or imp() or blanks_result() == True:
        gameplay = False
        return

board_display() 

gameplay = True 
      
while gameplay:
    win_check()
    current_turn = CHAR_X if current_turn == CHAR_O else CHAR_O
    handle_turn()
    win_check()
    board_display()
    win_check()
