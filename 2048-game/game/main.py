from services.game import Game
from board.board import Board

def main():
    board = Board()
    service = Game(board=board)

    commands = [1, 2, 3, 4]

    for command in commands:
        print(f'Executing command: {command}')
        service.start_service(command)

if __name__ == "__main__":
    main()

