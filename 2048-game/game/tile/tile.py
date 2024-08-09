class Tile():
    def __init__(self, value: int = 2) -> None:
        self._value = value
    
    def get_value(self) -> int:
        return self._value
    
    def set_value(self, value: int) -> None:
        self._value = value
