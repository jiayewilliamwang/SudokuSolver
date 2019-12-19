def solver(html_board, actual_board):
    for i in range(9):
        for j in range(9):
            if actual_board[i][j] == 0:
                for e in range(1, 10):
                    if is_valid(actual_board, i, j, e):
                        actual_board[i][j] = e
                        html_board[i][j].send_keys(e)
                        if solver(html_board, actual_board):
                            return True
                        else:
                            actual_board[i][j] = 0
                            html_board[i][j].clear()
                return False
    return True


def is_valid(board, row, col, cur):
    for i in range(9):
        if board[i][col] != 0 and board[i][col] == cur:
            return False
        if board[row][i] != 0 and board[row][i] == cur:
            return False
        sub_box = board[3 * (row // 3) + i // 3][ 3 * (col // 3) + i % 3]
        if sub_box != 0 and sub_box == cur:
            return False
    return True

