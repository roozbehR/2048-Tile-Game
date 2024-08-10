from game.board.board import Board
from game.services.game import Game

def main():
    board = Board()
    service = Game(board=board)
    service.start_service()

if __name__ == "__main__":
    main()

