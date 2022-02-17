#file deals with all the logic for the board
import numpy as np

#function that creates a board
def create_board(row, col):
    board = np.zeros((row, col))
    return board

#function that plays a piece of value at a certain board
def play_piece(board, row, col, piece_val):
    board[row][col] = piece_val 