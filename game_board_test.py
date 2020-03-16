import unittest
from cell import *
from game_board import *

class GameBoardTest(unittest.TestCase):
    def test_cell(self):
        names = (("no", "none"), ("no", "none"), ("ик", "икра"), ("но", "ножка"), ("пи", "пирог"), 
                ("по", "подлива"), ("пт", "птица"))
        classes = (Cell, EmptyCell, CaviarCell, ChickenLegCell, CakeCell, GravyCell, BirdCell)
        for cell, (short, full) in zip(classes, names):
            self.assertEqual(cell.get_short_name(), short)
            self.assertEqual(cell.get_full_name(), full)

    def test_board(self):
        board = GameBoard()
        empty_cell = board.get_empty_cells()
        self.assertEqual(empty_cell, ("11", "12", "13", "21", "22", "23"))
        cell = board.get_cell("11")
        self.assertEqual(cell, EmptyCell)
        self.assertEqual(cell.get_full_name(), "none")

        board.set_cell("11", CaviarCell)
        board.set_cell("21", ChickenLegCell)
        empty_cell = board.get_empty_cells()
        self.assertEqual(empty_cell, ("12", "13", "22", "23"))
        self.assertEqual(board.get_cell("11").get_full_name(), "икра")
        self.assertEqual(board.get_cell("21").get_full_name(), "ножка")

        board.set_cell("12", CakeCell)
        board.set_cell("13", CaviarCell)
        board.set_cell("22", GravyCell)
        board.set_cell("23", BirdCell)
        self.assertFalse(bool(board.get_empty_cells()))

        with self.assertRaises(WrongSelection):
            board.free_equal_cells("11", "12")
        self.assertFalse(bool(board.get_empty_cells()))
        # only top cells
        board.free_equal_cells("11", "13")
        self.assertEqual(board.get_empty_cells(), ("11", "13"))
        # only vertical cells
        board.set_cell("11", ChickenLegCell)
        board.set_cell("13", CaviarCell)
        board.free_equal_cells("11", "21")
        self.assertEqual(board.get_empty_cells(), ("11", "21"))
        # one down cell
        board.set_cell("11", GravyCell)
        board.set_cell("21", CakeCell)
        board.free_equal_cells("12", "21")
        self.assertEqual(board.get_empty_cells(), ("11", "12"))
        self.assertEqual(board.get_cell("21"), GravyCell)

if __name__ == "__main__":
    unittest.main()
