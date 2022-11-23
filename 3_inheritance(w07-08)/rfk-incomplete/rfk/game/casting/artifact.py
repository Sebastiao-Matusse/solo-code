from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
class Artifact(Actor):

    def __init__(self):
        super().__init__()
        
        self._message = ""

    def get_message(self):

        return self._message

    def set_message(self, message):
        """Gets the artifact's textual representation.
        
        Returns:
            string: The artifact's textual representation.
        """
        self._message = message
