__all__ = [
    "Cell",
    "EmptyCell",
    "CaviarCell",
    "ChickenLegCell",
    "CakeCell",
    "GravyCell",
    "BirdCell"
]

class Cell:
    _name = "none"

    @classmethod
    def get_full_name(cls):
        return cls._name

    @classmethod
    def get_short_name(cls):
        return cls.get_full_name()[:2]


class EmptyCell(Cell):
    pass

class CaviarCell(Cell):
    _name = "икра"

class ChickenLegCell(Cell):
    _name = "ножка"

class CakeCell(Cell):
    _name = "пирог"

class GravyCell(Cell):
    _name = "подлива"

class BirdCell(Cell):
    _name = "птица"