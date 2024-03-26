from regress.markers import BarMarker
from regress.markers import BAR_MARKERS
from regress.markers import SPINNER


class ProgressBar:

    filled_bar = "*"
    empty_bar = " "

    def __init__(self, max_value: int = 100, marker_string: str = "bar", bar_marker: BarMarker | None = None,
                 display_spinner: bool = True):
        self.max_value = max_value
        self.value = 0
        self.number_of_bars = 20
        self.interval = self.max_value / self.number_of_bars
        self.prefix = "Working"
        self.marker: BarMarker = bar_marker if isinstance(bar_marker, BarMarker) else BAR_MARKERS[marker_string]
        self.display_spinner = display_spinner

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
        if self.display_spinner:
            output = f"{next(SPINNER)} {output}"
        print(f"\r{output}", end="")
        return output


if __name__ == "__main__":
    import time


    class CustomMarker(BarMarker):

        @property
        def empty(self) -> str:
            return " "

        @property
        def filled(self) -> str:
            return "="


    p = ProgressBar(bar_marker=CustomMarker(), display_spinner=False)
    for i in range(p.max_value):
        p.update(i)
        time.sleep(0.3)
