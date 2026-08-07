import pygame
from chessVar import ChessVar

#
WIDTH, HEIGHT = 800, 800
SQUARE_SIZE = WIDTH // 8
BOARD_OFFSET = 35

LIGHT = (240, 217, 181)
DARK  = (181, 136, 99)

def draw_board(screen):
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                color = LIGHT
            else:
                color = DARK

            pygame.draw.rect(screen, color, (col * SQUARE_SIZE + BOARD_OFFSET, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

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
            
            screen.blit(image, (x + BOARD_OFFSET, y))
            
def draw_highlight(screen, selected_square):
    col_ind = ord(selected_square[0]) - ord('a')
    row_ind = 8 - int(selected_square[1])
    
    x = col_ind * SQUARE_SIZE
    y = row_ind * SQUARE_SIZE
    
    color = (255, 255, 0)
    
    pygame.draw.rect(screen, color, (x + BOARD_OFFSET, y, SQUARE_SIZE, SQUARE_SIZE))
    
def game_status(screen, game, invalid_move):
    font = pygame.font.SysFont(None, 40)
    text_color = (255, 255, 255)
    
    if game.get_game_state() != "UNFINISHED":
        if game.get_game_state() == "WHITE_WON":
            text = font.render("WHITE WON. Game over!", True, text_color)
        else:
            text = font.render("BLACK WON. Game over!", True, text_color)
    elif invalid_move == True:
            text = font.render(f"{game.get_turn()}: Invalid move. Try again.", True, text_color)
    else:
        text = font.render(f"{game.get_turn().capitalize()}'s turn", True, text_color)
    
    screen.blit(text, (10, HEIGHT + 60))
    
def draw_labels(screen):
    font = pygame.font.SysFont(None, 40)
    text_color = (255, 255, 255)
    
    for i, letter in enumerate('abcdefgh'):
        text = font.render(letter, True, text_color)

        x = i * SQUARE_SIZE + SQUARE_SIZE // 2
        y = HEIGHT + 5
        
        screen.blit(text, (x, y))
        
    for i, number in enumerate(range(8, 0, -1)):
        text = font.render(str(number), True, text_color)
        y = i * SQUARE_SIZE + SQUARE_SIZE // 2
        screen.blit(text, (8, y))
    
    
    
    

# run game
game = ChessVar()
pygame.init()
screen = pygame.display.set_mode((WIDTH + BOARD_OFFSET + 35, HEIGHT + 100))
pygame.display.set_caption("Chess")
reset_rect = pygame.Rect(WIDTH - 60, HEIGHT + 10, 80, 40)

reset_img = pygame.image.load("assets/reset.png")
reset_img = pygame.transform.scale(reset_img, (80, 40))
images = load_images()

# test
# print(game._chessboard['e1'].get_type())
# print(game._chessboard['e1'].get_color())
# game.make_move('e2', 'e4')

selected_square = None
invalid_move = False

while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            
            if reset_rect.collidepoint(x, y):
                print("Game reset.")
                game = ChessVar()
            else:
                col = (x - BOARD_OFFSET) // SQUARE_SIZE
                row = y // SQUARE_SIZE
                
                col_letter = chr(col + ord('a'))
                row_number = 8 - row
                square = col_letter + str(row_number)
                
                if selected_square is None:
                    selected_square = square
                else:
                    if not game.make_move(selected_square, square):
                        invalid_move = True
                    else:
                        invalid_move = False
                    selected_square = None
        
    draw_board(screen)
    draw_labels(screen)
    screen.blit(reset_img, (WIDTH - 60, HEIGHT + 60))
    if selected_square is not None:
        draw_highlight(screen, selected_square)
    draw_pieces(screen, images, game._chessboard)
    game_status(screen, game, invalid_move)
    pygame.display.flip()
        