from collections import namedtuple
from dataclasses import dataclass


@dataclass
class DataClassCard:
    rank: str
    suit: str


class RegularCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


@dataclass
class Position:
    name: str
    lon: float
    lat: float


if __name__ == "__main__":
    queen_of_hearts = DataClassCard("Q", "Hearts")
    print(queen_of_hearts.rank)
    print(queen_of_hearts.suit)
    print(queen_of_hearts == DataClassCard("Q", "Hearts"))

    regular_queen_of_hearts = RegularCard("Q", "Hearts")
    print(regular_queen_of_hearts.rank)
    print(regular_queen_of_hearts.suit)
    print(regular_queen_of_hearts == RegularCard("Q", "Hearts"))

    namedtuple_queen_of_hearts = namedtuple("Card", ["rank", "suit"])("Q", "Hearts")
    print(namedtuple_queen_of_hearts.rank)
    print(namedtuple_queen_of_hearts.suit)
