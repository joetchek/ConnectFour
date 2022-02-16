from re import S
import numpy as np
import pygame
import sys
import math 
from config import create_board, play_piece
from variables import *

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

def draw_board(screen, color):
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.circle(screen, color, (c*SQUARESIZE+SQUARESIZE/2, r*SQUARESIZE+SQUARESIZE/2),  RADIUS)
    
    pygame.display.update()


def draw_board_plays(screen, board):
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (c*SQUARESIZE+SQUARESIZE/2, r*SQUARESIZE+SQUARESIZE/2),  RADIUS)
            if board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (c*SQUARESIZE+SQUARESIZE/2, r*SQUARESIZE+SQUARESIZE/2),  RADIUS)

    pygame.display.update()


def check_for_events(screen):
    running = True
    while(running):
        draw_board(screen, BLACK)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
        

def main():
    board = create_board(ROW_COUNT, COL_COUNT)
    screen = create_screen()
    
    # board[1][1] = 1
    # board[2][2] = 2
    # draw_board_plays(screen, board)
    
    check_for_events(screen)


if __name__ == "__main__":
    main()

