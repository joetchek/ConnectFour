import numpy as np
import pygame
import sys
import math 
from config import create_board

def create_screen():
    #set bg color to black
    background_color = (0, 0, 0)

    #create the screen and set title 
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Connect Four game")

    #set bg color of screen
    screen.fill(background_color)

    #update the display 
    pygame.display.flip()

def check_for_events():
    running = True
    while(running):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

def main():
    create_screen()
    check_for_events()

if __name__ == "__main__":
    main()

