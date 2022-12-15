import constants


class Stats():

    def __init__(self):
        """Constructs a new Stats."""
        self._level = 0
        self._score = 0

    def add_points(self, points):
        """Adds the given points to the score.
        
        Args:
            points: A number representing the points to add.
        """
        self._score += points

    def get_level(self):
        """Gets the level.

        Returns:
            A number representing the level.
        """
        return self._level

    def get_score(self):
        """Gets the score.

        Returns:
            A number representing the score.
        """
        return self._score

    def next_level(self):
        """Adds one level."""
        self._level += 1
