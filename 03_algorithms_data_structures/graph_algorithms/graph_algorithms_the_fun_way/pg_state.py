class PGState:
    def __init__(
        self, guards_left: int = 3, prisoners_left: int = 3, boat_side: str = "L"
    ):
        self.guards_left = guards_left
        self.prisoners_left = prisoners_left
        self.boat_side = boat_side

    def __str__(self):
        return f"{self.guards_left},{self.prisoners_left},{self.boat_side}"
