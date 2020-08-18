def left_top_diagonal(coords):
    diagonal_coords_list = []

    (x, y) = coords
    while x >= 0 and y >= 0:
        if (x, y) != coords:
            diagonal_coords_list.append((x, y))
        x = x - 1
        y = y - 1

    return diagonal_coords_list


def right_top_diagonal(coords):
    diagonal_coords_list = []

    (x, y) = coords
    while x >= 0 and y <= 7:
        if (x, y) != coords:
            diagonal_coords_list.append((x, y))
        x = x - 1
        y = y + 1

    return diagonal_coords_list


def right_bottom_diagonal(coords):
    diagonal_coords_list = []

    (x, y) = coords
    while x <= 7 and y <= 7:
        if (x, y) != coords:
            diagonal_coords_list.append((x, y))
        x = x + 1
        y = y + 1

    return diagonal_coords_list


def left_bottom_diagonal(coords):
    diagonal_coords_list = []

    (x, y) = coords
    while x <= 7 and y >= 0:
        if (x, y) != coords:
            diagonal_coords_list.append((x, y))
        x = x + 1
        y = y - 1

    return diagonal_coords_list


def top_vertical(coords):
    vertical_coords_list = []

    (x, y) = coords
    while x >= 0:
        if (x, y) != coords:
            vertical_coords_list.append((x, y))
        x = x - 1

    return vertical_coords_list


def bottom_vertical(coords):
    vertical_coords_list = []

    (x, y) = coords
    while x <= 7:
        if (x, y) != coords:
            vertical_coords_list.append((x, y))
        x = x + 1

    return vertical_coords_list


def left_horizontal(coords):
    horizontal_coords_list = []

    (x, y) = coords
    while y >= 0:
        if (x, y) != coords:
            horizontal_coords_list.append((x, y))
        y = y - 1

    return horizontal_coords_list


def right_horizontal(coords):
    horizontal_coords_list = []

    (x, y) = coords
    while y <= 7:
        if (x, y) != coords:
            horizontal_coords_list.append((x, y))
        y = y + 1

    return horizontal_coords_list


def get_list_of_directions(coords, coords_figure_dict):
    list_of_directions = []

    # two lists so pawn can check for a beating move and no beating move
    vertical_directions_list = []
    diagonal_directions_list = []

    figure_name = coords_figure_dict[coords][1]
    figure_color = coords_figure_dict[coords][0]

    if figure_name == "queen" or figure_name == "king":
        list_of_directions = [left_top_diagonal(coords), right_top_diagonal(coords),
                              right_bottom_diagonal(coords), left_bottom_diagonal(coords),
                              left_horizontal(coords), right_horizontal(coords),
                              top_vertical(coords), bottom_vertical(coords)]
    elif figure_name == "rock":
        list_of_directions = [left_horizontal(coords), right_horizontal(coords),
                              top_vertical(coords), bottom_vertical(coords)]
    elif figure_name == "bishop":
        list_of_directions = [left_top_diagonal(coords), right_top_diagonal(coords),
                              right_bottom_diagonal(coords), left_bottom_diagonal(coords)]

    # pawn is getting a list, which contains two elements.
    # first one is list of vertical coords, second is list of diagonal coords
    elif figure_name == "pawn":
        # checking for a move without beating
        if figure_color == "white":
            vertical_directions_list = [bottom_vertical(coords)]
        elif figure_color == "red":
            vertical_directions_list = [top_vertical(coords)]

        # checking for a move with beating
        if figure_color == "white":
            diagonal_directions_list = [left_bottom_diagonal(coords), right_bottom_diagonal(coords)]
        elif figure_color == "red":
            diagonal_directions_list = [left_top_diagonal(coords), right_top_diagonal(coords)]

        list_of_directions.append(vertical_directions_list)
        list_of_directions.append(diagonal_directions_list)

    return list_of_directions


def get_pawn_moves(coords, coords_figure_dict):
    pawn_moves_list = []

    # checking for a move without beating
    direction = get_list_of_directions(coords, coords_figure_dict)[0][0]

    if len(direction) >= 1:
        # checking for a double jump
        if coords[0] == 1 and coords_figure_dict[coords][0] == "white":
            if coords_figure_dict[direction[0]] == ["0", "0"] and coords_figure_dict[direction[1]] == ["0", "0"]:
                pawn_moves_list.append(direction[1])
        elif coords[0] == 6 and coords_figure_dict[coords][0] == "red":
            if coords_figure_dict[direction[0]] == ["0", "0"] and coords_figure_dict[direction[1]] == ["0", "0"]:
                pawn_moves_list.append(direction[1])
        # checking for a single jump
        if coords_figure_dict[direction[0]] == ["0", "0"]:
            pawn_moves_list.append(direction[0])

    # checking for a move with beating
    list_of_directions = get_list_of_directions(coords, coords_figure_dict)[1]  # list of diagonal directions at 1

    for direction in list_of_directions:
        if len(direction) >= 1:
            if coords_figure_dict[direction[0]][0] == "white" and coords_figure_dict[coords][0] == "red":
                pawn_moves_list.append(direction[0])
            elif coords_figure_dict[direction[0]][0] == "red" and coords_figure_dict[coords][0] == "white":
                pawn_moves_list.append(direction[0])

    return pawn_moves_list


def get_line_moves(coords, coords_figure_dict):
    line_moves_list = []

    list_of_directions = get_list_of_directions(coords, coords_figure_dict)

    for direction in list_of_directions:
        # checking for a move without beating
        for square_to_move_to in direction:
            if coords_figure_dict[square_to_move_to] == ["0", "0"]:  # if the square is empty
                counter = 0
                x = 0
                while x < direction.index(square_to_move_to):
                    if coords_figure_dict[direction[x]] != ["0", "0"]:
                        counter += 1
                    x += 1
                if counter == 0:
                    line_moves_list.append(square_to_move_to)

        # checking for a move with beating
        for enemy in direction:
            if coords_figure_dict[enemy][0] != coords_figure_dict[coords][0] and coords_figure_dict[enemy] != ["0",
                                                                                                               "0"]:
                counter = 0
                x = 0
                while x < direction.index(enemy):
                    if coords_figure_dict[direction[x]] != ["0", "0"]:
                        counter += 1
                    x += 1
                if counter == 0:
                    line_moves_list.append(enemy)

    return line_moves_list


def get_king_moves(coords, coords_figure_dict):
    king_moves_list = []

    list_of_directions = get_list_of_directions(coords, coords_figure_dict)

    for direction in list_of_directions:
        # checking for a move without beating
        if len(direction) > 0:
            square_to_move_to = direction[0]
            if coords_figure_dict[square_to_move_to] == ["0", "0"]:  # if the square is empty
                king_moves_list.append(square_to_move_to)

        # checking for a move with beating
        if len(direction) > 0:
            enemy = direction[0]
            if coords_figure_dict[enemy][0] != coords_figure_dict[coords][0] and coords_figure_dict[enemy] != ["0",
                                                                                                               "0"]:
                king_moves_list.append(enemy)

    return king_moves_list


def get_knight_moves(coords, coords_figure_dict):
    knight_moves_list = []

    the_list = []

    if len(top_vertical(coords)) >= 2:
        two_squares_up_coords = top_vertical(coords)[1]
        if len(right_horizontal(two_squares_up_coords)) > 0:
            the_list.append(right_horizontal(two_squares_up_coords)[0])
        if len(left_horizontal(two_squares_up_coords)) > 0:
            the_list.append(left_horizontal(two_squares_up_coords)[0])

    if len(bottom_vertical(coords)) >= 2:
        two_squares_down_coords = bottom_vertical(coords)[1]
        if len(right_horizontal(two_squares_down_coords)) > 0:
            the_list.append(right_horizontal(two_squares_down_coords)[0])
        if len(left_horizontal(two_squares_down_coords)) > 0:
            the_list.append(left_horizontal(two_squares_down_coords)[0])

    if len(right_horizontal(coords)) >= 2:
        two_squares_right_coords = right_horizontal(coords)[1]
        if len(top_vertical(two_squares_right_coords)) > 0:
            the_list.append(top_vertical(two_squares_right_coords)[0])
        if len(bottom_vertical(two_squares_right_coords)) > 0:
            the_list.append(bottom_vertical(two_squares_right_coords)[0])

    if len(left_horizontal(coords)) >= 2:
        two_squares_left_coords = left_horizontal(coords)[1]
        if len(top_vertical(two_squares_left_coords)) > 0:
            the_list.append(top_vertical(two_squares_left_coords)[0])
        if len(bottom_vertical(two_squares_left_coords)) > 0:
            the_list.append(bottom_vertical(two_squares_left_coords)[0])

    for element in the_list:
        # no beating
        if coords_figure_dict[element] == ["0", "0"]:
            knight_moves_list.append(element)

        # beating
        elif coords_figure_dict[element][0] != coords_figure_dict[coords][0] and coords_figure_dict[element] != ["0",
                                                                                                                 "0"]:
            knight_moves_list.append(element)

    return knight_moves_list


def get_possible_moves_list(coords, coords_figure_dict):
    moves_list = []

    figure_name = coords_figure_dict[coords][1]

    if figure_name == "pawn":
        moves_list = get_pawn_moves(coords, coords_figure_dict)

    elif figure_name == "queen" or figure_name == "bishop" or figure_name == "rock":
        moves_list = get_line_moves(coords, coords_figure_dict)

    elif figure_name == "king":
        moves_list = get_king_moves(coords, coords_figure_dict)

    elif figure_name == "knight":
        moves_list = get_knight_moves(coords, coords_figure_dict)

    return moves_list

