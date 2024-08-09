from game.board import Board
from game.enums import Direction
from game.tile import Tile
from game.enums import Direction

class Game():
    def __init__(self, board: Board) -> None:
        self._board = board
        self._rows = self._board.get_rows()
        self._cols = self._board.get_cols()

    def start_service(self, command: str) -> None:
        direction = Direction(command)
        self.move(direction)
        self._board.print_board()
    
    def get_board(self) -> Board:
        return self._board

    def move(self, direction: Direction) -> None:
        if direction == Direction.UP:
            self.move_up()
        elif direction == Direction.DOWN:
            self.move_down()
        elif direction == Direction.LEFT:
            self.move_left()
        elif direction == Direction.RIGHT:
            self.move_right()
        else:
            raise ValueError("Invalid direction")
    
    def move_left(self) -> None:
        for row in range(self._rows):
            for col in range(1, self._cols):
                tile = self._board.get_tile(row, col)
                if tile:
                    self._move_tile_left(tile, row, col)
    
    def move_right(self) -> None:
        for row in range(self._rows):
            for col in range(self._cols - 2, -1, -1):
                tile = self._board.get_tile(row, col)
                if tile:
                    self._move_tile_right(tile, row, col)
    
    def move_up(self) -> None:
        for row in range(1, self._rows):
            for col in range(self._cols):
                tile = self._board.get_tile(row, col)
                if tile:
                    self._move_tile_up(tile, row, col)

    def move_down(self) -> None:
        for row in range(self._rows - 2, -1, -1):
            for col in range(self._cols):
                tile = self._board.get_tile(row, col)
                if tile:
                    self._move_tile_down(tile, row, col)

    def _move_tile_up(self, tile: Tile, row: int, col: int) -> None:
        for row in range(row - 1, -1, -1):
            t = self._board.get_tile(row, col)
            if t:
                if t.get_value() == tile.get_value():
                    self._board.remove_tile(tile, row, col)
                    self._board.remove_tile(t, row, col)
                    self._board.add_tile(Tile(tile.get_value() * 2), row, col)
                break
            else:
                self._board.remove_tile(tile, row + 1, col)
                self._board.add_tile(tile, row, col)

    def _move_tile_down(self, tile: Tile, row: int, col: int) -> None:
        for row in range(row + 1, self._rows):
            t = self._board.get_tile(row, col)
            if t:
                if t.get_value() == tile.get_value():
                    self._board.remove_tile(tile, row, col)
                    self._board.remove_tile(t, row, col)
                    self._board.add_tile(Tile(tile.get_value() * 2), row, col)
                break
            else:
                self._board.remove_tile(tile, row - 1, col)
                self._board.add_tile(tile, row, col)

    def _move_tile_left(self, tile: Tile, row: int, col: int) -> None:
        for col in range(col - 1, -1, -1):
            t = self._board.get_tile(row, col)
            if t:
                if t.get_value() == tile.get_value():
                    self._board.remove_tile(tile, row, col)
                    self._board.remove_tile(t, row, col)
                    self._board.add_tile(Tile(tile.get_value() * 2), row, col)
                break
            else:
                self._board.remove_tile(tile, row, col + 1)
                self._board.add_tile(tile, row, col)


    def _move_tile_right(self, tile: Tile, row: int, col: int) -> None:
        for col in range(col + 1, self._cols):
            t = self._board.get_tile(row, col)
            if t:
                if t.get_value() == tile.get_value():
                    self._board.remove_tile(tile, row, col)
                    self._board.remove_tile(t, row, col)
                    self._board.add_tile(Tile(tile.get_value() * 2), row, col)
                break
            else:
                self._board.remove_tile(tile, row, col - 1)
                self._board.add_tile(tile, row, col)
                
    
