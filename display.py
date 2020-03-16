from game_board import *
from cell import Cell, CaviarCell, ChickenLegCell, CakeCell, GravyCell, BirdCell

class Display:
    selectable_cells = (CaviarCell, ChickenLegCell, CakeCell, GravyCell, BirdCell)
    def __init__(self, auto_play = True):
        self._game_board = GameBoard()
        while auto_play:
            self.fill_empty_cells()
            self.print_board()
            self.free_cells()

    def print_board(self):
        print("|".join(["  ", *map(lambda c: str(c + 1).rjust(2), range(self._game_board.columns))]) + "|")

        for r in map(str, range(1, self._game_board.rows + 1)):
            line_list = [r.rjust(2)]
            for c in map(str, range(1, self._game_board.columns + 1)):
                line_list.append(self._game_board.get_cell(r + c).get_short_name().rjust(2))
            print("|".join(line_list) + "|")

    def select_cell(self) -> Cell:
        for i, c in enumerate(self.selectable_cells):
            print(f"{i + 1} {c.get_full_name()}")
        selection = ""
        while not (selection.isdigit() and 0 < int(selection) <= len(self.selectable_cells)):
            selection = input("Ваш выбор: ")
        return self.selectable_cells[int(selection) - 1]


    def free_cells(self):
        while True:
            pos1, pos2 = input("Введите две ячейки: ").split()
            try:
                self._game_board.free_equal_cells(pos1, pos2)
                break
            except WrongSelection as ex:
                print(str(ex))


    def fill_empty_cells(self):
        empty_cells = self._game_board.get_empty_cells()
        for pos in empty_cells:
            print(f"Выбор в ячейку {pos}: ")
            self._game_board.set_cell(pos, self.select_cell())


if __name__ == "__main__":
    Display()
