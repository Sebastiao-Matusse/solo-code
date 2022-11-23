import constants
from game.casting.score import Score
from game.shared.point import Point

class Score_2(Score):
    def __init__(self):
        super().__init__()
        self.set_color(constants.GREEN)
        self._position = Point(constants.MAX_X - 10, 0).scale(constants.CELL_SIZE)
        

    def add_points(self, points):
        self._points += points   
        self.set_text(f"Player Two: {self._points}")
    
