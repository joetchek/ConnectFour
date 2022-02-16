import numpy as np
import pygame
import sys
import math 
from config import create_board, play_piece
from variables import *

def create_screen():
    #set bg color to black
    background_color = (0, 0, 0)

    #create the screen and set title 
    screen = pygame.display.set_mode((ROW_COUNT*SQUARESIZE, COL_COUNT*SQUARESIZE))
    pygame.display.set_caption("Connect Four game")

    #set bg color of screen
    screen.fill(background_color)

    #update the display 
    pygame.display.flip()

    return screen

def draw_board(screen):
    radius = int(SQUARESIZE/2 - 5)
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (c*SQUARESIZE/2, r*SQUARESIZE*2),  radius)
    pygame.display.update()


def check_for_events():
    running = True
    while(running):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
        

def main():
    create_board(ROW_COUNT, COL_COUNT)
    screen = create_screen()
    draw_board(screen)
    check_for_events()


if __name__ == "__main__":
    main()

