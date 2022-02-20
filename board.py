#file deals with all the logic for the board
import numpy as np
from variables import *

#function that creates a board
def create_board(row, col):
    board = np.zeros((row, col))
    return board

#function that plays a piece of value at a certain board
def play_piece(board, row, col, piece_val):
    board[row][col] = piece_val 

#function that determines if a column is full
def is_column_full(col, board):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return False
    
    return True

#function that determines if the board is full
def is_board_full(board):
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 0:
                return False
    
    return True

#function that gets the highest avaliable row for a column to drop a piece
def get_highest_row(col, board):
    for r in reversed(range(ROW_COUNT)):
        if board[r][col] == 0:
            return r

#function that checks for possible win conditions
def check_for_win(board):
    pass