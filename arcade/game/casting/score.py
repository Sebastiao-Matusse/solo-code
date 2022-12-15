# import pygame
from constants import *
from game.casting.actor import Actor

class Score(Actor):
    def __init__(self) -> None:
        self._points = points
        self._time_passed = time_passed
        self._time_remaining = time_remaining

        
    def draw_score(self):
        points_text = font.render(f"Points: {self._points}", True, "black")
        screen.blit(points_text, (320, 660))
        shots_text = font.render(f"Total Shots {total_shots}", True, "black")
        screen.blit(shots_text, (320, 687))
        time_text = font.render(f"Time Elapsed: {time_passed}", True, "black")
        screen.blit(time_text, (320, 714))
        if mode == 0:
            mode_text = font.render(f"Freplay!", True, "black")
        elif mode == 1:
            mode_text = font.render(f"Ammo Remaining: {ammo}", True, "black")
        elif mode == 2:
            mode_text = font.render(f"Time Remaining: {time_remaining}", True, "black")
        screen.blit(mode_text, (320, 741))
