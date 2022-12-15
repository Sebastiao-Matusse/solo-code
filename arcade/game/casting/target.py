import pygame
from constants import *
from game.casting.actor import Actor
class Target(Actor):
   def __init__(self):
    self._target = []

    def set_target(self):
        for i in range(1, 4):
            bgs.append(pygame.image.load(f"arcade/assets/bgs/{i}.png"))
            banners.append(pygame.image.load(f"arcade/assets/banners/{i}.png"))
            guns.append(pygame.transform.scale(pygame.image.load(f"arcade/assets/guns/{i}.png"), (100, 100)))
            if i < 3:
                for j in range(1, 4):
                    target_images[i -1].append(pygame.transform.scale(
                        pygame.image.load(f"arcade/assets/targets/{i}/{j}.png"), (120 - (j*18), 80 - (j*12))))
            else:
                for j in range(1, 5):
                    target_images[i -1].append(pygame.transform.scale(
                        pygame.image.load(f"arcade/assets/targets/{i}/{j}.png"), (120 - (j*18), 80 - (j*12))))
