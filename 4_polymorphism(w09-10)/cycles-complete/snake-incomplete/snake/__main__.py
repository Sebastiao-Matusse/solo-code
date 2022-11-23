import constants

from game.casting.actor import Actor
from game.casting.cast import Cast
from game.casting.food import Food
from game.casting.score import Score
from game.casting.score_two import Score_2
from game.casting.snake import Snake
from game.casting.player_2 import Player_2
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.scripting.grow_player_tails_action import GrowPlayerTrailsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("player_one", Snake())
    cast.add_actor("player_two", Player_2())
    cast.add_actor("score_one", Score())
    cast.add_actor("score_two", Score_2())

    game_over = Actor()
    cast.add_actor("messages", game_over)
    cast.add_actor("foods", Food())
    # cast.add_actor("snakes", Snake())
    # cast.add_actor("snakes", Snake())
    # cast.add_actor("player_two", Player_2())
    # cast.add_actor("score_one", Score())
    # cast.add_actor("score_two", Score_2())
    # cast.get_first_actor("score_two")
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("update", GrowPlayerTrailsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()