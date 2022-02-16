import numpy as np

def create_board(row, col):
    board = np.zeros((row, col))
    return board

def play_piece(board, row, col, piece_val):
    board[row][col] = piece_val    

