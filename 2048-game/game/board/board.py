from typing import List, Tuple
from game.tile.tile import Tile

class Board():
    def __init__(self, rows: int = 4, cols: int = 4) -> None:
        self._rows = rows
        self._cols = cols
        self._board = [[None] * self._cols for _ in range(self._rows)]
        self._empty_tiles = [(row, col) for row in range(self._rows) for col in range(self._cols)]

    def get_rows(self) -> int:
        return self._rows
    
    def get_cols(self) -> int:
        return self._cols
    
    def get_tile(self, row: int, col: int) -> Tile:
        return self._board[row][col]

    def add_tile(self, tile: Tile, row: int, col: int) -> None:
        self._board[row][col] = tile
    
    def remove_tile(self, tile: Tile, row: int, col: int) -> None:
        self._board[row][col] = None

    def get_empty_tiles(self) -> List[Tuple[int, int]]:
        return self._empty_tiles
    
    def add_empty_tile(self, row: int, col: int) -> None:
        self._empty_tiles.append((row, col))

    def remove_empty_tile(self, row: int, col: int) -> None:
        self._empty_tiles.remove((row, col))

    def print_board(self) -> None:
        for row in self._board:
            row = [tile.get_value() if tile else '-' for tile in row]
            print(*row)