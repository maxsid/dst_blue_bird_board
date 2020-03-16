from cell import Cell, EmptyCell

__all__ = [
    "GameBoard",
    "WrongSelection"
]


class GameBoard:
    rows = 2
    columns = 3

    def __init__(self):
        self._cells = dict()
        for row in range(1, self.rows + 1):
            for column in range(1, self.columns + 1):
                self._cells[str(row) + str(column)] = EmptyCell

    def set_cell(self, pos: str, cell_class: type):
        if pos not in self._cells:
            raise KeyError(f"GameBoard doesn't have '{pos}' position.")
        if not issubclass(cell_class, Cell):
            raise TypeError("This isn't Cell class!")
        self._cells[pos] = cell_class

    def get_cell(self, pos: str) -> Cell:
        if pos not in self._cells:
            raise KeyError(f"GameBoard doesn't have '{pos}' position.")
        return self._cells[pos]

    def get_empty_cells(self):
        return tuple(sorted(filter(lambda p: self._cells[p] == EmptyCell, self._cells)))

    def free_equal_cells(self, pos1: str, pos2: str):
        if self.get_cell(pos1) != self.get_cell(pos2):
            raise WrongSelection("Cells must be equal!")
        self.free_cell(pos1)
        self.free_cell(pos2)

    def free_cell(self, pos: str):
        if pos.startswith("2"):
            pos2 = "1" + pos[-1]
            self.set_cell(pos, self.get_cell(pos2))
            self.set_cell(pos2, EmptyCell)
        else:
            self.set_cell(pos, EmptyCell)


class WrongSelection(Exception):
    pass
