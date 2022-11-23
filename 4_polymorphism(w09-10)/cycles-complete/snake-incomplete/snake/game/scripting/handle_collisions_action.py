import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_food_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_food_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score = cast.get_first_actor("score_one")
        food = cast.get_first_actor("foods")
        snake = cast.get_first_actor("player_one")
        head = snake.get_head()

        if head.get_position().equals(food.get_position()):
            points = food.get_points()
            snake.grow_tail(points)
            score.add_points(points)
            food.reset()

        score_2 = cast.get_first_actor("score_two")
        food = cast.get_first_actor("foods")
        player_two = cast.get_first_actor("player_two")
        head = player_two.get_head()

        if head.get_position().equals(food.get_position()):
            points = food.get_points()
            player_two.grow_tail(points)
            score_2.add_points(points)
            food.reset()
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        food = cast.get_first_actor("foods")
        score = cast.get_first_actor("score_one")
        score_two = cast.get_first_actor("score_two")


        # Player one collisions
        player_one = cast.get_first_actor("player_one")
        head = player_one.get_segments()[0]
        segments = player_one.get_segments()[1:]
        
        # Player two collisions
        player_two = cast.get_first_actor("player_two")
        player_two_head = player_two.get_segments()[0]
        player_two_segments = player_two.get_segments()[1:]

        for segment in segments:
            if head.get_position().equals(segment.get_position()):
                self._is_game_over = True

            if player_two_head.get_position().equals(segment.get_position()):
                score.add_points(1)
                self._is_game_over = True

        for segment in player_two_segments:
            if player_two_head.get_position().equals(segment.get_position()):
                self._is_game_over = True

        for segment in player_two_segments:
            if head.get_position().equals(segment.get_position()):
                score_two.add_points(1)
                self._is_game_over = True

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            snake = cast.get_first_actor("player_one")
            segments = snake.get_segments()
            food = cast.get_first_actor("foods")
            player_two = cast.get_first_actor("player_two")
            player_two_segments = player_two.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)
            for segment in player_two_segments:
                segment.set_color(constants.WHITE)
            food.set_color(constants.WHITE)
