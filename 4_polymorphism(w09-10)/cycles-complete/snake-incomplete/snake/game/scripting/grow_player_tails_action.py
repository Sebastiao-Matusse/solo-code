import constants
from game.scripting.action import Action

class GrowPlayerTrailsAction(Action):
  '''
  Grows each player's trail when the game is live.
  '''
  def execute(self, cast, script):
    message = cast.get_first_actor("messages")
    if message.get_text() == "":
      for actor in cast.get_actors("player_one"):
        actor.grow_tail(constants.SNAKE_LENGTH)
      for actor in cast.get_actors("player_two"):
        actor.grow_tail(constants.SNAKE_LENGTH)
    return