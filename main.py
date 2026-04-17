from chessVar import *

print("\nWelcome to this special Chess game. \n"
      "The rules are simple. Most rules of Chess apply except for the following:\n"
      " - No pawn promotion \n"
      " - No en passant \n"
      " - No check or checkmate"
      " - Only win by capturing the other king.")
print()

start = int(input("Ready to start? Press 1, or 0 to exit: "))
if start == 1:
      game = ChessVar()
      
      while game.get_game_state() == "UNFINISHED":
            game.display_board()
            turn = game.get_turn()
            move_from = input(f"{turn}'s turn. Enter the square to move from: ")
            move_to = input(f"Enter the square to move to: ")
            game.make_move(move_from, move_to)
      
      print(f"Game over! {game.get_game_state()}")
else:
      print("Thanks for playing!")