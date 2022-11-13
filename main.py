from itertools import combinations

row = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

points = [2, 7, 6, 9, 5, 1, 4, 3, 8]

# Initializes a board and is updated later on to show where a sign was put in. 
def current_board():
    string = ""
    for j in range(9):
        string +=  f"|{row[j]}"
        if j == 2 or j == 5 or j == 8 :
            string += "|\n" + "--+-+--\n"
    return string

# Check for correct inputs. Prevents signs to be overwritten.
def input_is_not_correct(x):
    if  int(x) not in points:
        print("Your input is incorrect, try again. It should be 'X'.Range (1-9). ")
        return True
    if row[int(x)-1] != " ":
        print("This spot is already filled. Please choose other one. ")
        return True

# Defines which players turn is it.
def where_to_input_sign(player):
    # Ask for current player's sign:
    x = input(f"Where do you want to put your {player}. Range(1-9): ")
    return (x)


# Should be cleaned up. Game flow is going through here.
def tic_tac_toe():

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
            x = where_to_input_sign(player)
            sign_on_board(x, player)

            # Appends player's collected points.
            points_x_lst.append(points[int(x)-1])
            if check_score(points_x_lst, player):
                return True

            # Switches turn to "O" player
            is_turn_x = False

        # Player's "O" turn
        if not is_turn_x:
            player = "O"

            # Asks wgere to put "O" sign
            x = where_to_input_sign(player) 
            sign_on_board(x, player)

            # Appends player's collected points.
            points_o_lst.append(points[int(x)-1])
            if check_score(points_o_lst, player):
                return True


# Put sign onto the board.
def sign_on_board(x, player):
    while input_is_not_correct(x):
        x= where_to_input_sign(player)
    row[int(x)-1] = player

# Draws can't be determined yet.
def check_score(point_list, player):
    print(current_board())
    if len(point_list) >=3 :
        # Goes through possible combinations of points in threes. And sums them up to see if they add up to 15. If they do. Player wins.
        if any(sum(comb)==15 for comb in combinations(point_list, 3)):
            print(f"Player with {player} won!")
            return True
        # If game is not resolved untill board is filled it is a draw.
        if len(point_list) >=5 :
            print(f"It's a draw!")
            return True


tic_tac_toe()



