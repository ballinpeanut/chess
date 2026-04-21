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

def load_images():
    colors = ['white', 'black']
    pieces = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']
    images = {}
    
    for color in colors:
        for piece in pieces:
          image = pygame.image.load(f"assets/chessPieces/{color}-{piece}.png")
          image = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE)) 
          images[f"{color}-{piece}"] = image 
    
    return images

def draw_pieces(screen, images, board):
    for square, piece in board.items():
        if piece is not None:
            piece_type = piece.get_type()
            piece_color = piece.get_color().lower()
            
            image = images[f"{piece_color}-{piece_type}"]
            
            col_ind = ord(square[0]) - ord('a')
            row_ind = 8 - int(square[1])
            
            x = col_ind * SQUARE_SIZE
            y = row_ind * SQUARE_SIZE
            
            screen.blit(image, (x, y))
            
def draw_highlight(screen, selected_square):
    col_ind = ord(selected_square[0]) - ord('a')
    row_ind = 8 - int(selected_square[1])
    
    x = col_ind * SQUARE_SIZE
    y = row_ind * SQUARE_SIZE
    
    color = (255, 255, 0)
    
    pygame.draw.rect(screen, color, (x, y, SQUARE_SIZE, SQUARE_SIZE))
    
    
    

# run game
game = ChessVar()
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

images = load_images()

# test
# print(game._chessboard['e1'].get_type())
# print(game._chessboard['e1'].get_color())
# game.make_move('e2', 'e4')

selected_square = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            col = x // SQUARE_SIZE
            row = y // SQUARE_SIZE
            
            col_letter = chr(col + ord('a'))
            row_number = 8 - row
            square = col_letter + str(row_number)
            
            if selected_square is None:
                selected_square = square
            else:
                game.make_move(selected_square, square)
                selected_square = None
        
    draw_board(screen)
    if selected_square is not None:
        draw_highlight(screen, selected_square)
    draw_pieces(screen, images, game._chessboard)
    pygame.display.flip()
        