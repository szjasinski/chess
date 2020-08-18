import tkinter as tk
from figure_normal_moves_functions import get_possible_moves_list

# TO DO: better images, solve status problem adter resetting game, improve code organization


class Chess(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        under_checkerboard_color = "#A6CFEA"
        my_frame = tk.Frame(parent, bg=under_checkerboard_color)


        # holds coords and a corresponding instances of buttons
        COORDS_BUTTON_DICT = {}

        # holds coords and a corresponding list, which contains color and type of figure (zeros if there isn't any figure)
        COORDS_FIGURE_DICT = {}  # ie {(0,0): ["white", "queen"], (1,1): ["red", "pawn"], (2,2): ["0", "0"]}

        # dictionary needed for following castling possibilities
        KING_ROCK_DIDNT_MOVE_DICT = {"white left": True, "white right": True, "red left": True, "red right": True}

        OLD_COORDS = (100, 100)  # generated when clicking a figure. holds coords of a figure to move
        IS_CLICKED = False
        WHITE_TURN = True
        IS_GAME_OVER = False
        TIMER_COUNTER = 0

        STATUS_LABEL = tk.Label(my_frame, text="turn: white", font=("Helvetica", 16), padx=10, pady=5)
        TIMER_LABEL = tk.Label(my_frame, text="00:00", font=("Helvetica", 16), padx=10, pady=5)


        # white_pawn_white_bg_image = PhotoImage(file="chess_img/white_bg/white_pawn_white_bg.png")
        white_pawn_white_bg_image = tk.PhotoImage(file="chess_img/white_bg/white_pawn_white_bg.png")
        white_rock_white_bg_image = tk.PhotoImage(file="chess_img/white_bg/white_rock_white_bg.png")
        white_knight_white_bg_image = tk.PhotoImage(file="chess_img/white_bg/white_knight_white_bg.png")
        white_bishop_white_bg_image = tk.PhotoImage(file="chess_img/white_bg/white_bishop_white_bg.png")
        white_king_white_bg_image = tk.PhotoImage(file="chess_img/white_bg/white_king_white_bg.png")
        white_queen_white_bg_image = tk.PhotoImage(file="chess_img/white_bg/white_queen_white_bg.png")

        white_pawn_grey_bg_image = tk.PhotoImage(file="chess_img/grey_bg/white_pawn_grey_bg.png")
        white_rock_grey_bg_image = tk.PhotoImage(file="chess_img/grey_bg/white_rock_grey_bg.png")
        white_knight_grey_bg_image = tk.PhotoImage(file="chess_img/grey_bg/white_knight_grey_bg.png")
        white_bishop_grey_bg_image = tk.PhotoImage(file="chess_img/grey_bg/white_bishop_grey_bg.png")
        white_king_grey_bg_image = tk.PhotoImage(file="chess_img/grey_bg/white_king_grey_bg.png")
        white_queen_grey_bg_image = tk.PhotoImage(file="chess_img/grey_bg/white_queen_grey_bg.png")

        white_bg = tk.PhotoImage(file="chess_img/white_bg/white_bg.png")

        red_pawn_white_bg_image = tk.PhotoImage(file="chess_img/white_bg/red_pawn_white_bg.png")
        red_rock_white_bg_image = tk.PhotoImage(file="chess_img/white_bg/red_rock_white_bg.png")
        red_knight_white_bg_image = tk.PhotoImage(file="chess_img/white_bg/red_knight_white_bg.png")
        red_bishop_white_bg_image = tk.PhotoImage(file="chess_img/white_bg/red_bishop_white_bg.png")
        red_king_white_bg_image = tk.PhotoImage(file="chess_img/white_bg/red_king_white_bg.png")
        red_queen_white_bg_image = tk.PhotoImage(file="chess_img/white_bg/red_queen_white_bg.png")

        red_pawn_grey_bg_image = tk.PhotoImage(file="chess_img/grey_bg/red_pawn_grey_bg.png")
        red_rock_grey_bg_image = tk.PhotoImage(file="chess_img/grey_bg/red_rock_grey_bg.png")
        red_knight_grey_bg_image = tk.PhotoImage(file="chess_img/grey_bg/red_knight_grey_bg.png")
        red_bishop_grey_bg_image = tk.PhotoImage(file="chess_img/grey_bg/red_bishop_grey_bg.png")
        red_king_grey_bg_image = tk.PhotoImage(file="chess_img/grey_bg/red_king_grey_bg.png")
        red_queen_grey_bg_image = tk.PhotoImage(file="chess_img/grey_bg/red_queen_grey_bg.png")

        grey_bg = tk.PhotoImage(file="chess_img/grey_bg/grey_bg.png")

        white_pawn_highlighted_image = tk.PhotoImage(file="chess_img/highlighted/white_pawn_highlighted.png")
        white_rock_highlighted_image = tk.PhotoImage(file="chess_img/highlighted/white_rock_highlighted.png")
        white_knight_highlighted_image = tk.PhotoImage(file="chess_img/highlighted/white_knight_highlighted.png")
        white_bishop_highlighted_image = tk.PhotoImage(file="chess_img/highlighted/white_bishop_highlighted.png")
        white_king_highlighted_image = tk.PhotoImage(file="chess_img/highlighted/white_king_highlighted.png")
        white_queen_highlighted_image = tk.PhotoImage(file="chess_img/highlighted/white_queen_highlighted.png")

        red_pawn_highlighted_image = tk.PhotoImage(file="chess_img/highlighted/red_pawn_highlighted.png")
        red_rock_highlighted_image = tk.PhotoImage(file="chess_img/highlighted/red_rock_highlighted.png")
        red_knight_highlighted_image = tk.PhotoImage(file="chess_img/highlighted/red_knight_highlighted.png")
        red_bishop_highlighted_image = tk.PhotoImage(file="chess_img/highlighted/red_bishop_highlighted.png")
        red_king_highlighted_image = tk.PhotoImage(file="chess_img/highlighted/red_king_highlighted.png")
        red_queen_highlighted_image = tk.PhotoImage(file="chess_img/highlighted/red_queen_highlighted.png")

        highlighted_bg = tk.PhotoImage(file="chess_img/highlighted/highlighted_bg.png")
        castling_highlighted_bg = tk.PhotoImage(file="chess_img/highlighted/castling_highlighted_bg.png")

        white_pawn_purple_bg_image = tk.PhotoImage(file="chess_img/purple_bg/white_pawn_purple_bg.png")
        white_rock_purple_bg_image = tk.PhotoImage(file="chess_img/purple_bg/white_rock_purple_bg.png")
        white_knight_purple_bg_image = tk.PhotoImage(file="chess_img/purple_bg/white_knight_purple_bg.png")
        white_bishop_purple_bg_image = tk.PhotoImage(file="chess_img/purple_bg/white_bishop_purple_bg.png")
        white_king_purple_bg_image = tk.PhotoImage(file="chess_img/purple_bg/white_king_purple_bg.png")
        white_queen_purple_bg_image = tk.PhotoImage(file="chess_img/purple_bg/white_queen_purple_bg.png")

        red_pawn_purple_bg_image = tk.PhotoImage(file="chess_img/purple_bg/red_pawn_purple_bg.png")
        red_rock_purple_bg_image = tk.PhotoImage(file="chess_img/purple_bg/red_rock_purple_bg.png")
        red_knight_purple_bg_image = tk.PhotoImage(file="chess_img/purple_bg/red_knight_purple_bg.png")
        red_bishop_purple_bg_image = tk.PhotoImage(file="chess_img/purple_bg/red_bishop_purple_bg.png")
        red_king_purple_bg_image = tk.PhotoImage(file="chess_img/purple_bg/red_king_purple_bg.png")
        red_queen_purple_bg_image = tk.PhotoImage(file="chess_img/purple_bg/red_queen_purple_bg.png")

        purple_bg = tk.PhotoImage(file="chess_img/purple_bg/purple_bg.png")

        white_bg_images_dict = {tuple(["white", "pawn"]): white_pawn_white_bg_image,
                                tuple(["white", "rock"]): white_rock_white_bg_image,
                                tuple(["white", "knight"]): white_knight_white_bg_image,
                                tuple(["white", "bishop"]): white_bishop_white_bg_image,
                                tuple(["white", "king"]): white_king_white_bg_image,
                                tuple(["white", "queen"]): white_queen_white_bg_image,
                                tuple(["red", "pawn"]): red_pawn_white_bg_image,
                                tuple(["red", "rock"]): red_rock_white_bg_image,
                                tuple(["red", "knight"]): red_knight_white_bg_image,
                                tuple(["red", "bishop"]): red_bishop_white_bg_image,
                                tuple(["red", "king"]): red_king_white_bg_image,
                                tuple(["red", "queen"]): red_queen_white_bg_image}

        grey_bg_images_dict = {tuple(["white", "pawn"]): white_pawn_grey_bg_image,
                               tuple(["white", "rock"]): white_rock_grey_bg_image,
                               tuple(["white", "knight"]): white_knight_grey_bg_image,
                               tuple(["white", "bishop"]): white_bishop_grey_bg_image,
                               tuple(["white", "king"]): white_king_grey_bg_image,
                               tuple(["white", "queen"]): white_queen_grey_bg_image,
                               tuple(["red", "pawn"]): red_pawn_grey_bg_image,
                               tuple(["red", "rock"]): red_rock_grey_bg_image,
                               tuple(["red", "knight"]): red_knight_grey_bg_image,
                               tuple(["red", "bishop"]): red_bishop_grey_bg_image,
                               tuple(["red", "king"]): red_king_grey_bg_image,
                               tuple(["red", "queen"]): red_queen_grey_bg_image}

        purple_bg_images_dict = {tuple(["white", "pawn"]): white_pawn_purple_bg_image,
                                 tuple(["white", "rock"]): white_rock_purple_bg_image,
                                 tuple(["white", "knight"]): white_knight_purple_bg_image,
                                 tuple(["white", "bishop"]): white_bishop_purple_bg_image,
                                 tuple(["white", "king"]): white_king_purple_bg_image,
                                 tuple(["white", "queen"]): white_queen_purple_bg_image,
                                 tuple(["red", "pawn"]): red_pawn_purple_bg_image,
                                 tuple(["red", "rock"]): red_rock_purple_bg_image,
                                 tuple(["red", "knight"]): red_knight_purple_bg_image,
                                 tuple(["red", "bishop"]): red_bishop_purple_bg_image,
                                 tuple(["red", "king"]): red_king_purple_bg_image,
                                 tuple(["red", "queen"]): red_queen_purple_bg_image}

        highlighted_images_dict = {tuple(["white", "pawn"]): white_pawn_highlighted_image,
                                   tuple(["white", "rock"]): white_rock_highlighted_image,
                                   tuple(["white", "knight"]): white_knight_highlighted_image,
                                   tuple(["white", "bishop"]): white_bishop_highlighted_image,
                                   tuple(["white", "king"]): white_king_highlighted_image,
                                   tuple(["white", "queen"]): white_queen_highlighted_image,
                                   tuple(["red", "pawn"]): red_pawn_highlighted_image,
                                   tuple(["red", "rock"]): red_rock_highlighted_image,
                                   tuple(["red", "knight"]): red_knight_highlighted_image,
                                   tuple(["red", "bishop"]): red_bishop_highlighted_image,
                                   tuple(["red", "king"]): red_king_highlighted_image,
                                   tuple(["red", "queen"]): red_queen_highlighted_image}


        def do_nothing():
            pass


        def disable_figures():
            for coords in COORDS_BUTTON_DICT:
                COORDS_BUTTON_DICT[coords].config(command=do_nothing)

        def reset_board():
            nonlocal IS_CLICKED
            nonlocal IS_GAME_OVER
            nonlocal WHITE_TURN
            nonlocal TIMER_COUNTER
            nonlocal KING_ROCK_DIDNT_MOVE_DICT

            IS_CLICKED = False
            WHITE_TURN = True
            IS_GAME_OVER = False
            TIMER_COUNTER = 0
            KING_ROCK_DIDNT_MOVE_DICT = {"white left": True, "white right": True, "red left": True, "red right": True}

            construct_buttons()
            construct_figures()


        def update_status():
            if WHITE_TURN:
                turn_txt = "turn: white "
            else:
                turn_txt = "turn: red "
            status_txt = turn_txt

            # getting list of coords of the kings
            kings_coords_list = []
            for coords, figure in COORDS_FIGURE_DICT.items():
                if figure[1] == "king":
                    kings_coords_list.append(coords)

            for coords in kings_coords_list:
                if is_square_attacked(coords, COORDS_FIGURE_DICT):
                    king_color = COORDS_FIGURE_DICT[coords][0]
                    if IS_GAME_OVER:
                        status_txt = king_color + " king CHECKEDMATED"

                    else:
                        status_txt = turn_txt + " &  " + king_color + " king CHECKED"

            STATUS_LABEL.config(text=status_txt)
            STATUS_LABEL.grid(row=8, column=3, columnspan=4)

        def update_timer():
            nonlocal TIMER_COUNTER

            TIMER_COUNTER += 1

            minutes = (TIMER_COUNTER // 60)
            seconds = TIMER_COUNTER

            if minutes > 0:
                for x in range(0, minutes):
                    seconds = seconds - 60

            if minutes < 10:
                minutes_str = "0" + str(minutes)
            else:
                minutes_str = str(minutes)

            if seconds < 10:
                seconds_str = "0" + str(seconds)
            else:
                seconds_str = str(seconds)

            game_time = minutes_str + ":" + seconds_str

            if not IS_GAME_OVER:
                TIMER_LABEL.config(text=game_time)
                TIMER_LABEL.after(1000, update_timer)

        def get_image(coords):
            key = tuple(COORDS_FIGURE_DICT[coords])
            if (coords[0] + coords[1]) % 2 == 1:
                img = grey_bg_images_dict[key]
            else:
                img = white_bg_images_dict[key]

            return img

        def highlight_images(coords):
            # coloring picked figure purple
            figure = tuple(COORDS_FIGURE_DICT[coords])
            img = purple_bg_images_dict[figure]
            COORDS_BUTTON_DICT[coords].config(image=img)

            # coloring possible moves green
            for element in get_all_possible_moves(coords, COORDS_FIGURE_DICT):
                if COORDS_FIGURE_DICT[element] == ["0", "0"]:  # if there is no figure
                    # if the figure is king, there is a separate highlighting for a castling move
                    if figure[1] == "king":
                        king_squares_to_castle_to = [(0, 2), (0, 6), (7, 6), (7, 2)]
                        if element in king_squares_to_castle_to:
                            COORDS_BUTTON_DICT[element].config(image=castling_highlighted_bg)
                        else:
                            COORDS_BUTTON_DICT[element].config(image=highlighted_bg)
                    # standard highlighting
                    else:
                        COORDS_BUTTON_DICT[element].config(image=highlighted_bg)
                else:  # if there is a figure
                    figure = tuple(COORDS_FIGURE_DICT[element])
                    img = highlighted_images_dict[figure]
                    COORDS_BUTTON_DICT[element].config(image=img)

        def unhighlight_images():
            for element in COORDS_FIGURE_DICT:
                if COORDS_FIGURE_DICT[element] == ["0", "0"]:  # if there is no figure
                    if (element[0] + element[1]) % 2 == 1:
                        COORDS_BUTTON_DICT[element].config(image=grey_bg)
                    else:
                        COORDS_BUTTON_DICT[element].config(image=white_bg)
                else:  # if there is a figure
                    img = get_image(element)
                    COORDS_BUTTON_DICT[element].config(image=img)

        def get_king_castling_moves(coords, coords_figure_dict):
            king_castling_moves = []
            enemy_dict = {"white": "red", "red": "white"}

            king_coords = coords
            king_color = coords_figure_dict[king_coords][0]
            enemy_color = enemy_dict[king_color]

            castling_attributes_dict = {"white left": [[(0, 1), (0, 2), (0, 3)], (0, 3), (0, 2)],
                                        "white right": [[(0, 5), (0, 6)], (0, 5), (0, 6)],
                                        "red right": [[(7, 5), (7, 6)], (7, 5), (7, 6)],
                                        "red left": [[(7, 1), (7, 2), (7, 3)], (7, 3), (7, 2)]}

            for castling_version, king_rock_not_moved in KING_ROCK_DIDNT_MOVE_DICT.items():
                if king_rock_not_moved:
                    coords_between = castling_attributes_dict[castling_version][0]
                    square_walked_by = castling_attributes_dict[castling_version][1]
                    square_to_castle_to = castling_attributes_dict[castling_version][2]

                    # checking for no figures between king and rock
                    no_figures_between = False
                    count = 0
                    for element in coords_between:
                        if coords_figure_dict[element] == ["0", "0"]:
                            count += 1
                    if count == len(coords_between):
                        no_figures_between = True

                    if no_figures_between:
                        # checking if king is not attacked
                        if not is_square_attacked(king_coords, coords_figure_dict):
                            # checking if square, which king walks over is not being attacked
                            if square_walked_by not in get_squares_attacked_by_color(enemy_color, COORDS_FIGURE_DICT):
                                # checking if king will not be attacked after castling
                                if square_to_castle_to not in get_squares_attacked_by_color(enemy_color, COORDS_FIGURE_DICT):
                                    king_castling_moves.append(square_to_castle_to)

            return king_castling_moves

        def update_kings_castling_possibilities():
            # update KING_ROCK_DIDNT_MOVE_DICT

            king_color_coords_dict = {"white": (0, 4), "red": (7, 4)}
            left_rock_color_coords_dict = {"white": (0, 0), "red": (7, 0)}
            right_rock_color_coords_dict = {"white": (0, 7), "red": (7, 7)}

            for color in king_color_coords_dict:

                starting_king_coords = king_color_coords_dict[color]
                starting_left_rock_coords = left_rock_color_coords_dict[color]
                starting_right_rock_coords = right_rock_color_coords_dict[color]

                if color == "white":
                    # check if king has moved
                    if COORDS_FIGURE_DICT[starting_king_coords][1] != "king":
                        KING_ROCK_DIDNT_MOVE_DICT["white left"] = False
                        KING_ROCK_DIDNT_MOVE_DICT["white right"] = False
                    # check if rocks have moved
                    if COORDS_FIGURE_DICT[starting_left_rock_coords][1] != "rock":
                        KING_ROCK_DIDNT_MOVE_DICT["white left"] = False
                    if COORDS_FIGURE_DICT[starting_right_rock_coords][1] != "rock":
                        KING_ROCK_DIDNT_MOVE_DICT["white right"] = False

                elif color == "red":
                    # check if king has moved
                    if COORDS_FIGURE_DICT[starting_king_coords][1] != "king":
                        KING_ROCK_DIDNT_MOVE_DICT["red left"] = False
                        KING_ROCK_DIDNT_MOVE_DICT["red right"] = False
                    # check if rocks have moved
                    if COORDS_FIGURE_DICT[starting_left_rock_coords][1] != "rock":
                        KING_ROCK_DIDNT_MOVE_DICT["red left"] = False
                    if COORDS_FIGURE_DICT[starting_right_rock_coords][1] != "rock":
                        KING_ROCK_DIDNT_MOVE_DICT["red right"] = False

        def get_coords_of_figures_which_can_be_moved_to_save_king_and_their_moves_dict(king_coords):
            enemy_dict = {"white": "red", "red": "white"}
            king_color = COORDS_FIGURE_DICT[king_coords][0]

            figure_coords_to_save_king_and_their_moves_dict = {}
            for element in COORDS_FIGURE_DICT:
                # for a figure in king color, which isnt the king
                if COORDS_FIGURE_DICT[element][0] == king_color and COORDS_FIGURE_DICT[element][1] != "king":
                    figure_moves = get_possible_moves_list(element, COORDS_FIGURE_DICT)
                    for move in figure_moves:
                        temporary_coords_figure_dict = COORDS_FIGURE_DICT.copy()
                        temporary_coords_figure_dict[move] = COORDS_FIGURE_DICT[element]
                        temporary_coords_figure_dict[element] = ["0", "0"]

                        attacked_by_enemy_after_beating = get_squares_attacked_by_color(enemy_dict[king_color],
                                                                                        temporary_coords_figure_dict)

                        if king_coords not in attacked_by_enemy_after_beating:
                            figure_coords_to_save_king_and_their_moves_dict[element] = move

            return figure_coords_to_save_king_and_their_moves_dict

        def get_king_moves_to_safety(king_coords):
            enemy_dict = {"white": "red", "red": "white"}

            king_color = COORDS_FIGURE_DICT[king_coords][0]
            defending_king_moves = get_possible_moves_list(king_coords, COORDS_FIGURE_DICT)

            kings_moves_attacked_by_enemy = []
            for king_move in defending_king_moves:
                temporary_coords_figure_dict = COORDS_FIGURE_DICT.copy()
                temporary_coords_figure_dict[king_move] = [king_color, "king"]
                temporary_coords_figure_dict[king_coords] = ["0", "0"]

                squares_attacked_after_kings_move = get_squares_attacked_by_color(enemy_dict[king_color],
                                                                                  temporary_coords_figure_dict)

                if king_move in squares_attacked_after_kings_move:
                    kings_moves_attacked_by_enemy.append(king_move)

            king_moves_to_safety = []
            for move in defending_king_moves:
                if move not in kings_moves_attacked_by_enemy:
                    king_moves_to_safety.append(move)

            return king_moves_to_safety

        def get_squares_attacked_by_color(color, coords_figure_dict):
            attacked_by_color_list = []

            for element in coords_figure_dict:
                if coords_figure_dict[element][0] == color:
                    list_of_moves = get_possible_moves_list(element, coords_figure_dict)
                    for move in list_of_moves:
                        if move not in attacked_by_color_list:  # remove duplicates of square attacked by multiple enemy figures
                            attacked_by_color_list.append(move)

            return attacked_by_color_list

        def is_square_attacked(coords, coords_figure_dict):
            enemy_dict = {"white": "red", "red": "white"}

            defender_color = coords_figure_dict[coords][0]
            print("defender_color", defender_color)
            print("enemy_dict[defender_color]", enemy_dict[defender_color])
            attacked_by_enemy = get_squares_attacked_by_color(enemy_dict[defender_color], coords_figure_dict)

            if coords in attacked_by_enemy:
                return True

            return False

        def win_check():
            nonlocal IS_GAME_OVER
            winner = "none"
            king_coords = "x"

            enemy_dict = {"white": "red", "red": "white"}

            if not IS_GAME_OVER:
                for color in enemy_dict:
                    for coords, figure in COORDS_FIGURE_DICT.items():
                        if figure == [color, "king"]:
                            king_coords = coords

                    if is_square_attacked(king_coords, COORDS_FIGURE_DICT):
                        if len(get_coords_of_figures_which_can_be_moved_to_save_king_and_their_moves_dict(king_coords)) == 0 \
                                and len(get_king_moves_to_safety(king_coords)) == 0:
                            winner = enemy_dict[color]
                            IS_GAME_OVER = True

            if IS_GAME_OVER:
                disable_figures()

            print("the winner is", winner)
            print("     ")

        def get_all_possible_moves(coords, coords_figure_dict):
            all_moves_list = []
            is_king_attacked = False

            # getting coords of the king to check if he is attacked
            color = COORDS_FIGURE_DICT[coords][0]
            for element, figure in COORDS_FIGURE_DICT.items():
                if figure == [color, "king"]:
                    defending_king_coords = element
            if is_square_attacked(defending_king_coords, coords_figure_dict):
                is_king_attacked = True

            # getting moves list
            if is_king_attacked:
                the_dict = get_coords_of_figures_which_can_be_moved_to_save_king_and_their_moves_dict(defending_king_coords)
                # getting moves of a figure if it is a figure that can save king
                for element, move in the_dict.items():
                    if coords == element:
                        all_moves_list.append(move)
                # getting moves of a king if it is a king
                if coords_figure_dict[coords][1] == "king":
                    all_moves_list = get_king_moves_to_safety(defending_king_coords)
            else:
                # get standard moves of a figure
                standard_moves_list = get_possible_moves_list(coords, coords_figure_dict)
                print("standard moves", standard_moves_list)

                # if the figure is king, get castling moves and moves that won't make him CHECKED
                figure_name = coords_figure_dict[coords][1]
                if figure_name == "king":
                    castling_moves_list = get_king_castling_moves(coords, coords_figure_dict)
                    print("castling moves", castling_moves_list)

                    all_moves_list = get_king_moves_to_safety(coords) + castling_moves_list
                else:
                    all_moves_list = standard_moves_list

            return all_moves_list

        def move_rock_if_castling(new_coords):
            all_possible_moves_list = get_all_possible_moves(OLD_COORDS, COORDS_FIGURE_DICT)
            standard_possible_moves_list = get_possible_moves_list(OLD_COORDS, COORDS_FIGURE_DICT)

            castling_version_king_squares_to_castle_to_dict = {"white left": (0, 2), "white right": (0, 6),
                                                               "red right": (7, 6), "red left": (7, 2)}

            castling_version_starting_rock_coords_dict = {"white left": (0, 0), "white right": (0, 7),
                                                          "red right": (7, 7), "red left": (7, 0)}

            castling_version_rock_squares_to_castle_to_dict = {"white left": (0, 3), "white right": (0, 5),
                                                               "red right": (7, 5), "red left": (7, 3)}

            # if the figure is king and there is a castling possibility
            if all_possible_moves_list != standard_possible_moves_list:
                for castling_version, square_to_castle_to in castling_version_king_squares_to_castle_to_dict.items():
                    # if the castling is happening
                    if new_coords == square_to_castle_to:
                        rock_starting_coords = castling_version_starting_rock_coords_dict[castling_version]
                        rock_to_move_coords = castling_version_rock_squares_to_castle_to_dict[castling_version]

                        COORDS_FIGURE_DICT[rock_to_move_coords] = COORDS_FIGURE_DICT[rock_starting_coords]
                        COORDS_FIGURE_DICT[rock_starting_coords] = ["0", "0"]

                        # drawing rock in new place and removing it from old place
                        img = get_image(rock_to_move_coords)
                        COORDS_BUTTON_DICT[rock_to_move_coords].config(image=img)
                        if (rock_starting_coords[0] + rock_starting_coords[1]) % 2 == 1:
                            COORDS_BUTTON_DICT[rock_starting_coords].config(image=grey_bg)
                        else:
                            COORDS_BUTTON_DICT[rock_starting_coords].config(image=white_bg)

        def move_figure(new_coords):
            # move figure from OLD_COORDS to new_coords

            all_possible_moves_list = get_all_possible_moves(OLD_COORDS, COORDS_FIGURE_DICT)

            if new_coords in all_possible_moves_list:

                move_rock_if_castling(new_coords)

                # checking and changing pawn into a queen
                if COORDS_FIGURE_DICT[OLD_COORDS][1] == "pawn" and (new_coords[0] == 0 or new_coords[0] == 7):
                    COORDS_FIGURE_DICT[new_coords][0] = COORDS_FIGURE_DICT[OLD_COORDS][0]
                    COORDS_FIGURE_DICT[new_coords][1] = "queen"
                    COORDS_FIGURE_DICT[OLD_COORDS] = ["0", "0"]

                # making a normal move
                else:
                    COORDS_FIGURE_DICT[new_coords] = COORDS_FIGURE_DICT[OLD_COORDS]
                    COORDS_FIGURE_DICT[OLD_COORDS] = ["0", "0"]

                # drawing figure in new place and removing it from old place
                img = get_image(new_coords)
                COORDS_BUTTON_DICT[new_coords].config(image=img)
                if (OLD_COORDS[0] + OLD_COORDS[1]) % 2 == 1:
                    COORDS_BUTTON_DICT[OLD_COORDS].config(image=grey_bg)
                else:
                    COORDS_BUTTON_DICT[OLD_COORDS].config(image=white_bg)

                make_turns(new_coords)

        def make_turns(new_coords):
            nonlocal WHITE_TURN

            color_of_moved_figure = COORDS_FIGURE_DICT[new_coords][0]
            if color_of_moved_figure == "white":
                WHITE_TURN = False
            else:
                WHITE_TURN = True

        def my_click(coords):
            nonlocal IS_CLICKED
            nonlocal OLD_COORDS

            if not IS_CLICKED:
                if COORDS_FIGURE_DICT[coords] != ["0", "0"]:  # if there is a figure at this coords
                    if (COORDS_FIGURE_DICT[coords][0] == "white" and WHITE_TURN) \
                            or (COORDS_FIGURE_DICT[coords][0] == "red" and not WHITE_TURN):
                        OLD_COORDS = coords
                        highlight_images(coords)
                        IS_CLICKED = True

            else:
                new_coords = coords
                move_figure(new_coords)
                update_kings_castling_possibilities()
                unhighlight_images()
                win_check()
                update_status()
                IS_CLICKED = False

        def construct_buttons():
            nonlocal STATUS_LABEL
            nonlocal TIMER_LABEL

            grid_count = 0
            for x in range(0, 8):
                for y in range(0, 8):
                    btn = tk.Button(my_frame, image=white_bg,
                                 command=lambda row_n=x, column_n=y: my_click((row_n, column_n)))
                    COORDS_BUTTON_DICT[(x, y)] = btn
                    COORDS_BUTTON_DICT[(x, y)].grid(row=x, column=y)
                    grid_count += 1

            for coords in COORDS_BUTTON_DICT:
                if (coords[0] + coords[1]) % 2 == 1:
                    COORDS_BUTTON_DICT[coords].config(image=grey_bg)

            reset_button = tk.Button(my_frame, text="reset board", font=("Helvetica", 16), padx=20, pady=10,
                                  command=reset_board)
            reset_button.grid(row=8, column=0, columnspan=3, padx=20, pady=10)

            STATUS_LABEL = tk.Label(my_frame, text="turn: white", font=("Helvetica", 16), padx=10, pady=5)
            STATUS_LABEL.grid(row=8, column=3, columnspan=4)

            game_time = "00:00"
            TIMER_LABEL = tk.Label(my_frame, text=game_time, font=("Helvetica", 16), padx=10, pady=5)
            TIMER_LABEL.grid(row=8, column=7)

        def construct_figures():
            nonlocal COORDS_FIGURE_DICT

            COORDS_FIGURE_DICT = COORDS_BUTTON_DICT.copy()

            for coords in COORDS_FIGURE_DICT:
                if coords[0] == 1:
                    COORDS_FIGURE_DICT[coords] = ["white", "pawn"]
                elif coords[0] == 0:
                    if coords[1] == 0 or coords[1] == 7:
                        COORDS_FIGURE_DICT[coords] = ["white", "rock"]
                    elif coords[1] == 1 or coords[1] == 6:
                        COORDS_FIGURE_DICT[coords] = ["white", "knight"]
                    elif coords[1] == 2 or coords[1] == 5:
                        COORDS_FIGURE_DICT[coords] = ["white", "bishop"]
                    elif coords[1] == 3:
                        COORDS_FIGURE_DICT[coords] = ["white", "queen"]
                    elif coords[1] == 4:
                        COORDS_FIGURE_DICT[coords] = ["white", "king"]

                elif coords[0] == 6:
                    COORDS_FIGURE_DICT[coords] = ["red", "pawn"]
                elif coords[0] == 7:
                    if coords[1] == 0 or coords[1] == 7:
                        COORDS_FIGURE_DICT[coords] = ["red", "rock"]
                    elif coords[1] == 1 or coords[1] == 6:
                        COORDS_FIGURE_DICT[coords] = ["red", "knight"]
                    elif coords[1] == 2 or coords[1] == 5:
                        COORDS_FIGURE_DICT[coords] = ["red", "bishop"]
                    elif coords[1] == 3:
                        COORDS_FIGURE_DICT[coords] = ["red", "queen"]
                    elif coords[1] == 4:
                        COORDS_FIGURE_DICT[coords] = ["red", "king"]

                else:
                    COORDS_FIGURE_DICT[coords] = ["0", "0"]

            for coords in COORDS_FIGURE_DICT:
                if COORDS_FIGURE_DICT[coords] != ["0", "0"]:
                    img = get_image(coords)
                    COORDS_BUTTON_DICT[coords].config(image=img)

        construct_buttons()
        construct_figures()
        TIMER_LABEL.after(1000, update_timer)
        my_frame.pack()


if __name__ == "__main__":
    root = tk.Tk()
    root.title('CHESS')
    Chess(root).pack()
    root.mainloop()
