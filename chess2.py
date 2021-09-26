import chess_lib
import numpy as np
import sys, pygame
from pygame.locals import *

SCREENRECT = pygame.Rect(0, 0, 800, 600)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

def main():
    # Initialize pygame module
    pygame.init()

	# Load/scale board image and get its size
    board_sprite = pygame.image.load('assets/board.png')
    for i in range(2):
        board_sprite = pygame.transform.scale2x(board_sprite)
    board_size = np.array(board_sprite.get_size())

    # Create the screen
    winstyle = 0
    bestdepth = pygame.display.mode_ok(board_size, winstyle, 32)
    screen = pygame.display.set_mode(board_size, winstyle, bestdepth)

    # Create board bounds as sub-surface of board
    board_bounds_size = np.array(board_sprite.get_size()) * .995
    board_bounds = board_sprite.subsurface((0,0), board_bounds_size)
    # TODO: Fill board bounds with red transparency
    board_bounds.set_colorkey(red)
    board_bounds.set_alpha(20)
    board_bounds.fill(red)

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
