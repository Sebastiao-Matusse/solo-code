import constants
from game.casting.cast import Cast
from game.casting.snake import Snake
from game.shared.point import Point
from game.casting.actor import Actor

class Player_2(Snake):

    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        super().__init__()

    def grow_tail(self, number_of_segments):
        cast = Cast()
        # message = cast.get_first_actor("messages")
        message = cast.get_first_actor("messages")

        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            # if message.get_text() == "":
            #     for i in self._segments:
            segment.set_color(constants.GREEN)
            self._segments.append(segment)

    def _prepare_body(self):
        x = int(constants.MAX_X - 300)
        y = int(constants.MAX_Y - 100)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = constants.GREEN
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)
