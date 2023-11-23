def solution(board):
    board = "".join(board)
    board_1 = board.count("O")
    board_2 = board.count("X")
    bingo_1 = False
    bingo_2 = False
    
    if board_1 < board_2:
        return 0
    if board_1 - board_2 > 1:
        return 0
    if board[0] == 'O' and board[4] == 'O' and board[8] == 'O':
        bingo_1 = True
    if board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
        bingo_2 = True
    if board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
        bingo_1 = True
    if board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
        bingo_2 = True
    if board[0] == 'O' and board[1] == 'O' and board[2] == 'O':
        bingo_1 = True
    if board[3] == 'O' and board[4] == 'O' and board[5] == 'O':
        bingo_1 = True
    if board[6] == 'O' and board[7] == 'O' and board[8] == 'O':
        bingo_1 = True
    if board[0] == 'X' and board[1] == 'X' and board[2] == 'X':
        bingo_2 = True
    if board[3] == 'X' and board[4] == 'X' and board[5] == 'X':
        bingo_2 = True
    if board[6] == 'X' and board[7] == 'X' and board[8] == 'X':
        bingo_2 = True
    if board[0] == 'O' and board[3] == 'O' and board[6] == 'O':
        bingo_1 = True
    if board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
        bingo_1 = True
    if board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
        bingo_1 = True
    if board[0] == 'X' and board[3] == 'X' and board[6] == 'X':
        bingo_2 = True
    if board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
        bingo_2 = True
    if board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
        bingo_2 = True
        
    if bingo_1 == True and bingo_2 == True: return 0
    if bingo_1 == True and board_1 <= board_2: return 0
    if bingo_2 == True and board_1 != board_2: return 0
    
    return 1