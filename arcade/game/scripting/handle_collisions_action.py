from constants import *
from game.services.audio_service import *
from game.scripting.action import Action
from game.services.video_service import VideoService
# from game.shared.point import Point

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
        self._is_game_over = True
        self._clicked = True
        self._pause = False
        self._menu = True
        self._new_coords = new_coords
        self._level = level
        self._points = points
        self._points = 0
        self._total_shots = 0
        self._time_passed = 0
        self._time_remaining = 0
        self._video_service = VideoService()
        

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            # self._handle_food_collision(cast)
            self._check_shot(targets, one_coords)
            self._check_shot(targets, two_coords)
            self._check_shot(targets, three_coords)
            self._handle_game_over(cast)

    def _handle_food_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
    def _check_shot(targets, coords):

        """Checks the collision between the mouse and the targets, and eliminates that target
        
        Args:
            targets (Targets): The """
        # mouse_pos = pygame.mouse.get_pos()
        for i in range(len(targets)):
            for j in range(len(targets[i])):
                if targets[i][j].collidepoint(mouse_position):
                    coords[i].pop(j)
                    points += 10 + 10 * (i**2)
                    if level == 1:
                        bird_sound.play()
                    elif level == 2:
                        plate_sound.play()
                    elif level == 3:
                        laser_sound.play()
        return coords

    def check_pause(self):
        resume_level = self._level
        VideoService.draw_menu(pause_img)
        resume_button = VideoService.draw_button((170, 661), (260, 100))
        # resume_button = pygame.rect.Rect((170, 661), (260, 100))
        menu_button = VideoService.draw_button((475, 661), (260, 100))
        # menu_button = pygame.rect.Rect((475, 661), (260, 100))
        if resume_button.collidepoint(mouse_position) and clicks[0] and not clicked:
            self._level = resume_level
            self._pause = False
            self._clicked = True
        if menu_button.collidepoint(mouse_position) and clicks[0] and not clicked:
            pygame.mixer.music.play()
            self._level = 0
            self._pause = 0
            self._menu = True
            self._points = 0
            self._total_shots = 0
            self._time_passed = 0
            self._time_remaining = 0
            self._clicked = True
            self._new_coords = True

    def _handle_game_over(self):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if mode == 0:
            display_score = time_passed
        else:
            display_score = points
        screen.blit(game_over_img, (0, 0))
        screen.blit(big_font.render(f"{display_score}", True, "black"), (650, 570))
        if menu_button.collidepoint(mouse_position) and clicks[0] and not clicked:
            self._clicked = True
            self._level = 0
            self._pause = False
            self._is_game_over = False
            self._menu = True
            self._points = 0
            self._total_shots = 0
            self._time_passed = 0
            self._time_remaining = 0
        if exit_button.collidepoint(mouse_position) and clicks[0] and not clicked:
            self._run = False
