# row list is used to define a playboard and points are assigned to these fields. Once a player reaches 15 points it means that he won.
row = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
points = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]

winning_scenarios = [[i[j] for i in points] for j in range(0,3) ]
print(winning_scenarios)
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
def where_to_input_sign(player):
    # if sign_is_x:
    x, y = input(f"Where do you want to put your {player}:").strip().split(" ")
    return int(x), int(y)
    # if not sign_is_x:
    #     x, y = input("Where do you want to put your O:").strip().split(" ")
    #     return int(x), int(y)

# Should be cleaned up. Game flow is going through here.
def input_x_or_o():
    # Players' collected points
    points_x_lst = []
    points_o_lst = []
    print(current_board())
    game_is_on = True
    while game_is_on:
        # When true it is "X" turn
        is_turn_x = True
        if is_turn_x:
            player = "X"
            # Asks wgere to put "O" sign
            x, y = where_to_input_sign(player)
            sign_on_board(x, y, player)
            points_x_lst.append(points[int(x)-1][int(y)-1])
            if check_score(points_x_lst, player):
                return True
            # Switches turn to "O" player
            is_turn_x = False
        # Player's "O" turn
        if not is_turn_x:
            player = "O"
            # Asks wgere to put "O" sign
            x, y = where_to_input_sign(player) 
            sign_on_board(x, y, player)
            points_o_lst.append(points[int(x)-1][int(y)-1])
            if check_score(points_o_lst, player):
                return True


# Put sign onto the board.
def sign_on_board(x, y, player):
    while input_is_not_correct(x, y):
        x, y = where_to_input_sign(is_turn_x)
    row[int(x)-1][int(y)-1] = player

# Draws needs to be sorted out
def check_score(point_list, player):
    print(current_board())
    if len(point_list) >=3 :
        for number in point_list:
            total_points = sum(point_list)
            if total_points == 15:
                print(current_board())
                print(f"Player with {player} won!")
                return True
            if total_points - number == 15:
                print(current_board())
                print(f"Player with {player} won!")
                return True
        if len(point_list) == 5:
            print("It's a draw")
            return True

input_x_or_o()



