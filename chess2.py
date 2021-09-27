import chess_lib
import numpy as np
import sys, pygame
from pygame.locals import *

SCREENSIZE = (400, 400)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

def main():
    # Initialize pygame module
    pygame.init()

    # Create the screen
    # TODO: Investigate these settings
    winstyle = 0
    bestdepth = pygame.display.mode_ok(SCREENSIZE, winstyle, 32)
    screen = pygame.display.set_mode(SCREENSIZE, winstyle, bestdepth)

	# Load/scale board image and get its size
    board_sprite = pygame.image.load('assets/board.png')
    board_size = SCREENSIZE
    board_sprite = pygame.transform.scale(board_sprite, board_size)

    # Create board bounds as sub-surface of board
    board_bounds = pygame.Surface((400, 400))
    # TODO: Fill board bounds with red transparency
    board_bounds.fill(RED)
    board_bounds.set_alpha(50)
    # Draw board_bounds on board
    board_sprite.blit(board_bounds, (0, 0))
    # Erase the surface
    board_bounds.set_colorkey(WHITE)
    board_bounds.fill(WHITE)

    # TODO: Squares as sub-surfaces of board bounds
    # square_size = board_size * 0.125
    # square = board_bounds.subsurface((0,0), square_size)
    # square.fill(red)
    # for file in range(8):
    #     for rank in range(8):
    #         square = 

    # Loading images
    w_king_sprite = pygame.image.load('assets/white_king.png')
    w_queen_sprite = pygame.image.load('assets/white_queen.png')
    w_rook_sprite = pygame.image.load('assets/white_rook.png')
    w_bishop_sprite = pygame.image.load('assets/white_bishop.png')
    w_knight_sprite = pygame.image.load('assets/white_knight.png')
    w_pawn_sprite = pygame.image.load('assets/white_pawn.png')
    b_king_sprite = pygame.image.load('assets/black_king.png')
    b_queen_sprite = pygame.image.load('assets/black_queen.png')
    b_rook_sprite = pygame.image.load('assets/black_rook.png')
    b_bishop_sprite = pygame.image.load('assets/black_bishop.png')
    b_knight_sprite = pygame.image.load('assets/black_knight.png')
    b_pawn_sprite = pygame.image.load('assets/black_pawn.png')

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(board_sprite, (0, 0))
        pygame.display.flip()

if __name__=="__main__":
    main()
