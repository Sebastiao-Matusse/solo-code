from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
class Gem(Actor):

    def __init__(self):
        super().__init__()
        
        self._points = 0

    def get_points(self):

        return self._points

    def set_points(self, points):
        """Gets the gem's points.
        
        Returns:
            int: The gem's points.
        """
        self._points = points 
