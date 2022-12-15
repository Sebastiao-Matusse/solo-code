from time import sleep
import constants
from game.shared.point import Point
from game.casting.actor import Actor

class Timer(Actor):
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
        self._counter = 15
        self._position = Point(constants.MAX_X - 10, 2).scale(constants.CELL_SIZE)
        # service = VideoService()
        self._time_passed = 0
        self._set_time()

    def _set_time(self):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        if self._time_passed != 1:
            if self._counter < 12:
                self._counter += 1
                sleep(1)
            else:
                self._counter = 1   

        self.set_text(f"Time Passed: {self._counter}")
