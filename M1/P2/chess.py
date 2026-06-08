def position_to_coords(pos):
    column = ord(pos[0].lower()) - ord('a') + 1
    row = int(pos[1])
    return column, row

def is_within_board(col, row):
    return 1 <= col <= 8 and 1 <= row <= 8

def is_valid_rook(start, end):
    start_col, start_row = position_to_coords(start)
    end_col, end_row = position_to_coords(end)
    if not is_within_board(end_col, end_row):
        return False
    if start == end:
        return False
    return start_col == end_col or start_row == end_row

def is_valid_bishop(start, end):
    start_col, start_row = position_to_coords(start)
    end_col, end_row = position_to_coords(end)
    return abs(start_col - end_col) == abs(start_row - end_row)

def is_valid_knight(start, end):
    start_col, start_row = position_to_coords(start)
    end_col, end_row = position_to_coords(end)
    col_diff = abs(start_col - end_col)
    row_diff = abs(start_row - end_row)
    return (col_diff, row_diff) in [(2, 1), (1, 2)]

def is_valid_move(piece, start, end):
    piece = piece.lower()
    if piece == "rock":
        return is_valid_rook(start, end)
    elif piece == "bishop":
        return is_valid_bishop(start, end)
    elif piece == "knight":
        return is_valid_knight(start, end)
    else:
        return False