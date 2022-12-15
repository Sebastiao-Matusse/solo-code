import constants
from game.shared.point import Point
from game.casting.actor import Actor
from game.casting.score import Score


class BestScore(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        self._best_score = self.get_best_score()
        score = Score()
        self._points = score.get_points()
        # self.add_points(0)
        self._position = Point(constants.MAX_X - 10, 0).scale(constants.CELL_SIZE)
        self.set_best_score()
        self.get_best_score()
        self.write_values()

    def get_best_score(self):
        file = open("snake/high_scores.txt", "r")
        read_file = file.readlines()
        file.close
        self._best_score = int(read_file[0])
        
        return self._best_score

    def set_best_score(self):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self.set_text(f"Last best Score: {self._points}")

    def write_values(self):
        if self._points > self._best_score:
            file = open("snake/high_scores.txt", "w")
            file.write(f"{self._points}")
            file.close()
