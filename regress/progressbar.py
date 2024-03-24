from regress.markers import BarMarker
from regress.markers import BAR_MARKERS


class ProgressBar:

    filled_bar = "*"
    empty_bar = " "

    def __init__(self, max_value: int = 100, marker: str = "asterisk"):
        self.max_value = max_value
        self.value = 0
        self.number_of_bars = 20
        self.interval = self.max_value / self.number_of_bars
        self.prefix = "Working"
        self.marker: BarMarker = BAR_MARKERS[marker]

    def update(self, completed: int) -> str:
        self.value = completed
        bars_completed = int(self.value / self.max_value * self.number_of_bars)
        bars_remaining = self.number_of_bars - bars_completed
        bar_string = (
            f"{self.marker.filled * bars_completed}{self.marker.empty * bars_remaining}"
        )
        postfix = (
            f"{self.value}/{self.max_value} [{round(self.value / self.max_value * 100)}%]"
        )
        output = f"{self.prefix} {bar_string} {postfix}"
        print(f"\r{output}", end="")
        return output
