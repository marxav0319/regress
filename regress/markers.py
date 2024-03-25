from abc import ABCMeta
from abc import abstractmethod
from itertools import cycle


class BarMarker(metaclass=ABCMeta):

    @abstractmethod
    def empty(self) -> str:
        pass

    @abstractmethod
    def filled(self) -> str:
        pass


class Asterisk(BarMarker):

    @property
    def empty(self) -> str:
        return " "

    @property
    def filled(self) -> str:
        return "*"


class Square(BarMarker):

    @property
    def empty(self) -> str:
        return "\u25fb"

    @property
    def filled(self) -> str:
        return "\u25fc"


class Rectangle(BarMarker):

    @property
    def empty(self) -> str:
        return "\u25af"

    @property
    def filled(self) -> str:
        return "\u25ae"


class Bar(BarMarker):

    @property
    def empty(self) -> str:
        return "\u2582"

    @property
    def filled(self) -> str:
        return "\u2587"


BAR_MARKERS = {
    "asterisk": Asterisk(),
    "square": Square(),
    "rectangle": Rectangle(),
    "bar": Bar()
}

SPINNER = cycle(
    [
        "\u25D0",
        "\u25D1",
        "\u25D2",
        "\u25D3",
    ]
)
