import pygame
from chessVar import ChessVar

#
WIDTH, HEIGHT = 800, 800
SQUARE_SIZE = WIDTH // 8

LIGHT = (240, 217, 181)
DARK  = (181, 136, 99)

def draw_board(screen):
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                color = LIGHT
            else:
                color = DARK

            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


# run game
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
    draw_board(screen)
    pygame.display.flip()
        