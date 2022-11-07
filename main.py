# row list is used to define a playboard and points are assigned to these fields. Once a player reaches 15 points it means that he won.
row = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
points = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]

# Initializes a board and is updated later on to show where a sign was put in. 
def current_board():
    string = ""
    for j in range(3):
        for i in range(3):
            string +=  f"|{row[j][i]}"
        string += "|\n" + "--+-+--\n"
    return string

# Check for correct inputs. Prevents signs to be overwritten.
def input_is_not_correct(x, y):
    if  int(x) not in {1, 2 ,3} or  int(y) not in {1, 2, 3}:
        print("Your input is incorrect, try again. It should be 'X Y' (eg. 1 2).")
        return True
    if row[int(x)-1][int(y)-1] == "X" or  row[int(x)-1][int(y)-1] == "O":
        print("This spot is already filled. Please choose other one")
        return True

# Defines which players turn is it.
def input_sign(sign):
    if sign:
        x, y = input("Where do you want to put your X:").strip().split(" ")
        return int(x), int(y)
    if not sign:
        x, y = input("Where do you want to put your O:").strip().split(" ")
        return int(x), int(y)

# Should be cleaned up. Game flow is going through here.
def input_x_or_o():
    points_x = 0
    points_o = 0
    print(current_board())
    game_is_on = True
    while game_is_on:
        turn_x = True
        if turn_x:
            x, y = input_sign(turn_x)
            while input_is_not_correct(x, y):
                x, y = input_sign(turn_x)
            row[int(x)-1][int(y)-1] = "X"
            points_x += points[int(x)-1][int(y)-1]
            board = current_board()
            if points_x == 15:
                print(board)
                print("Player with X won!")
                break
            print(board)
            turn_x = False
        if not turn_x:
            x, y = input_sign(turn_x)
            while input_is_not_correct(x, y):
                x, y = input_sign(turn_x)
            row[int(x)-1][int(y)-1] = "O"
            points_o += points[int(x)-1][int(y)-1]
            board = current_board()
            if points_o == 15:
                print(board)
                print("Player with O won!")
                break
            print(board)


input_x_or_o()



