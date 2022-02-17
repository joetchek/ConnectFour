#file deals with all the logic for the game and the main
import numpy as np
import pygame
import math
from board import *
from variables import *

#function that creates the screen
def create_screen():
    #set bg color to black
    background_color = BLUE

    #create the screen and set title
    screen = pygame.display.set_mode((COL_COUNT*SQUARESIZE, ROW_COUNT*SQUARESIZE))
    pygame.display.set_caption("Connect Four game")

    #set bg color of screen
    screen.fill(background_color)

    #update the display
    pygame.display.flip()

    return screen

#function that draws the circles on the board all one color
def draw_board(screen, color):
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.circle(screen, color, (c*SQUARESIZE+SQUARESIZE/2, r*SQUARESIZE+SQUARESIZE/2),  RADIUS)

    pygame.display.update()

#function that draws the board plays in realtime
def draw_board_plays(screen, board):
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 0:
                pygame.draw.circle(screen, BLACK, (c*SQUARESIZE+SQUARESIZE/2, r*SQUARESIZE+SQUARESIZE/2),  RADIUS)
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (c*SQUARESIZE+SQUARESIZE/2, r*SQUARESIZE+SQUARESIZE/2),  RADIUS)
            if board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (c*SQUARESIZE+SQUARESIZE/2, r*SQUARESIZE+SQUARESIZE/2),  RADIUS)

    pygame.display.update()

#function that deals with the logic of tracking the mouse for highlighting the column
def mouse_track(board, board2, turn_val, mouse_x):
    if 0 <= mouse_x <= 100:
        board[0][0] = turn_val
    elif board2[0][0] != turn_val:
        board[0][0] = 0

    if 101 <= mouse_x <= 200:
        board[0][1] = turn_val
    elif board2[0][1] != turn_val:
        board[0][1] = 0

    if 201 <= mouse_x <= 300:
        board[0][2] = turn_val
    elif board2[0][2] != turn_val:
        board[0][2] = 0

    if 301 <= mouse_x <= 400:
        board[0][3] = turn_val
    elif board2[0][3] != turn_val:
        board[0][3] = 0

    if 401 <= mouse_x <= 500:
        board[0][4] = turn_val
    elif board2[0][4] != turn_val:
        board[0][4] = 0

    if 501 <= mouse_x <= 600:
        board[0][5] = turn_val
    elif board2[0][5] != turn_val:
        board[0][5] = 0

    if 601 <= mouse_x <= 700:
        board[0][6] = turn_val
    elif board2[0][6] != turn_val:
        board[0][6] = 0

#function that deals with all my realtime events
def check_for_events(screen, board, board2):
    running = True
    turn_val = 1 #determining player 1 or 2
    draw_board(screen, BLACK)
    while(running):
        for event in pygame.event.get():

            mouse = pygame.mouse.get_pos()
            mouse_x = mouse[0]

            if turn_val == 1:
                mouse_track(board, board2, turn_val, mouse_x)
            elif turn_val == 2:
                mouse_track(board, board2, turn_val, mouse_x)

            if event.type == pygame.QUIT:
                running = False
        #redraw board plays on every board
        draw_board_plays(screen, board)

#main 
def main():
    #board that manages the draw engine
    draw_board = create_board(ROW_COUNT, COL_COUNT)
    #this board tracks what pieces were played where
    play_board = create_board(ROW_COUNT, COL_COUNT)
    screen = create_screen()

    # board[3][1] = 1
    # board[5][2] = 2

    check_for_events(screen, draw_board, play_board)


if __name__ == "__main__":
    main()