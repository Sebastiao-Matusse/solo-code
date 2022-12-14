from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        
        # draw scores
        score_one = cast.get_first_actor("score_one")
        score_two = cast.get_first_actor("score_two")
        # draw players
        food = cast.get_first_actor("foods")
        player_one = cast.get_first_actor("player_one")
        # segments = player_one.get_segments()
        player_two = cast.get_first_actor("player_two")
        segments_player_two = player_two.get_segments()
        messages = cast.get_actors("messages")

        segments = []
        for segment in player_one.get_segments():
            segments.append(segment)
    

        self._video_service.clear_buffer()
        # self._video_service.draw_actor(food)
        self._video_service.draw_actors(segments)
        self._video_service.draw_actors(segments_player_two)
        self._video_service.draw_actor(score_one)
        self._video_service.draw_actor(score_two)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()