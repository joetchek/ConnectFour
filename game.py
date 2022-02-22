#file deals with all the logic for the game and the main
import pygame
import math
from board import *
from variables import *

#function that creates the screen
def create_screen():
    #set bg color to black
    background_color = BLUE

    #create the screen and set title
    screen = pygame.display.set_mode((COL_COUNT*SQUARESIZE, (ROW_COUNT+1)*SQUARESIZE))
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
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (c*SQUARESIZE+SQUARESIZE/2, r*SQUARESIZE+SQUARESIZE/2),  RADIUS)
            if board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (c*SQUARESIZE+SQUARESIZE/2, r*SQUARESIZE+SQUARESIZE/2),  RADIUS)

    pygame.display.update()

#function that deals with the logic of tracking the mouse for underlining the column
def mouse_track(screen, turn_val, column):
    color = BLACK
    if turn_val == 1:
        color = RED
    if turn_val == 2:
        color = YELLOW

    if column == 0:
        pygame.draw.rect(screen, color, (0, 600, SQUARESIZE, SQUARESIZE/20))
    else:
        pygame.draw.rect(screen, BLUE, (0, 600, SQUARESIZE, SQUARESIZE/20))

    if column == 1:
        pygame.draw.rect(screen, color, (100, 600, SQUARESIZE, SQUARESIZE/20))
    else:
        pygame.draw.rect(screen, BLUE, (100, 600, SQUARESIZE, SQUARESIZE/20))

    if column == 2:
        pygame.draw.rect(screen, color, (200, 600, SQUARESIZE, SQUARESIZE/20))
    else:
        pygame.draw.rect(screen, BLUE, (200, 600, SQUARESIZE, SQUARESIZE/20))

    if column == 3:
        pygame.draw.rect(screen, color, (300, 600, SQUARESIZE, SQUARESIZE/20))
    else:
        pygame.draw.rect(screen, BLUE, (300, 600, SQUARESIZE, SQUARESIZE/20))

    if column == 4:
        pygame.draw.rect(screen, color, (400, 600, SQUARESIZE, SQUARESIZE/20))
    else:
        pygame.draw.rect(screen, BLUE, (400, 600, SQUARESIZE, SQUARESIZE/20))

    if column == 5:
        pygame.draw.rect(screen, color, (500, 600, SQUARESIZE, SQUARESIZE/20))
    else:
        pygame.draw.rect(screen, BLUE, (500, 600, SQUARESIZE, SQUARESIZE/20))

    if column == 6:
        pygame.draw.rect(screen, color, (600, 600, SQUARESIZE, SQUARESIZE/20))
    else:
        pygame.draw.rect(screen, BLUE, (600, 600, SQUARESIZE, SQUARESIZE/20))

    pygame.display.update()
    
def print_winner(screen, turn_val, myfont):
    txt = "Player " + str(turn_val) + " wins!"
    render_txt = myfont.render(txt, 1, BLACK)
    screen.blit(render_txt, ((ROW_COUNT*SQUARESIZE)/2 - SQUARESIZE*2 - 65, (COL_COUNT-1)*SQUARESIZE+10))

#function that deals with all my realtime events
def check_for_events(screen, board):
    running = True
    turn_val = 1 #determining player 1 or 2
    draw_board(screen, BLACK)
    game_over = False
    myfont = pygame.font.SysFont("monospace", 75)
    while(running):
        for event in pygame.event.get():
            
            #tracks mouse position
            mouse = pygame.mouse.get_pos()
            mouse_x = mouse[0]
            current_col = math.floor(mouse_x/100)

            #constanly tracking the mouse position and drawing the appropriate underline
            #disables and deletes the mouse tracker when gameover
            if not game_over:
                mouse_track(screen, turn_val, current_col)
            else:
                pygame.draw.rect(screen, BLUE, (current_col*SQUARESIZE, 600, SQUARESIZE, SQUARESIZE/20))
                pygame.display.update()

            #when the mouse is pressed 
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                #check if column is full
                if not is_column_full(current_col, board):
                    #get row to play in
                    r_pos = get_highest_row(current_col, board) 
                    #plays a piece
                    play_piece(board, r_pos, current_col, turn_val)

                    #checks for win condition
                    if check_for_win(board):
                        print_winner(screen, turn_val, myfont)
                        game_over = True
                    #checks if the board is full if no win condition
                    elif is_board_full(board):
                        txt = myfont.render("Board Full!", 1, BLACK)
                        screen.blit(txt, ((ROW_COUNT*SQUARESIZE)/2 - SQUARESIZE*2, (COL_COUNT-1)*SQUARESIZE+10))
                        game_over = True

                    #switches the turn
                    if turn_val == 1:
                        turn_val = 2
                    elif turn_val == 2:
                        turn_val = 1

            if event.type == pygame.QUIT:
                running = False
        #redraw board plays on every board
        draw_board_plays(screen, board)

#main 
def main():
    #init the game
    pygame.init()
    #making the board
    board = create_board(ROW_COUNT, COL_COUNT)
    #creating the screen
    screen = create_screen()
    #run check for events
    check_for_events(screen, board)

if __name__ == "__main__":
    main()