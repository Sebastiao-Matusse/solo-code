from constants import *
import math


class Gun():
    """A solid, spherical object that is bounced around in the game."""
    
    def __init__(self, debug = False):
        """Constructs a new Gun.

        Args:
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)

    def get_gun(self):
        gun = pygame.transform.flip(guns[level - 1], True, False)
        return gun
    
    def draw_gun(self):
        if mouse_position[0] != gun_point[0]:
            slope = (mouse_position[1] - gun_point[0]) / (mouse_position[0] - gun_point[0])
        else:
            slope = -10000
        angle = math.atan(slope)
        rotation = math.degrees(angle)
        if mouse_position[0] < WIDTH/2:
            gun = pygame.transform.flip(guns[level - 1], True, False)
            if mouse_position[1] < 600:
                screen.blit(pygame.transform.rotate(gun, 90 - rotation), (WIDTH/2 - 90, HEIGHT - 250))
                if clicks[0]:
                    pygame.draw.circle(screen, lasers[level - 1], mouse_position, 5)
        else:
            gun = guns[level - 1]
            if mouse_position[1] < 600:
                screen.blit(pygame.transform.rotate(gun, 270 - rotation), (WIDTH/2 - 30, HEIGHT - 250))
                if clicks[0]:
                    pygame.draw.circle(screen, lasers[level - 1], mouse_position, 5)
