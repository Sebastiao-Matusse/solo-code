from constants import *
import pygame

class VideoService():
    def __init__(self):
        self._pause = pause
        self._clicks = clicks
        self._level = level
        self._menu = menu
        self._time_passed = time_passed
        self._clicked = clicked
        self._points = points
        self._total_shots = total_shots
        self._new_coords = new_coords
        self._ammo = ammo
        self.freeplay_button = None
        self.timed_button = None
        self.ammo_button = None
        self.reset_button = None

    def draw_menu(self, image):
        screen.blit(image, (0, 0))
    
    def draw_button(self, x_0, y_0, x_1, y_1):
        self._button = pygame.rect.Rect((x_0, y_0), (x_1, y_1))

    def draw_img_menu(self, image):
        screen.blit(image, (0, 0))
        screen.blit(font.render(f"{best_freeplay}", True, "black"), (340, 580))
        screen.blit(font.render(f"{best_ammo}", True, "black"), (650, 580))
        screen.blit(font.render(f"{best_timed}", True, "black"), (350, 710))
        if self.freeplay_button.collidepoint(mouse_position) and self._clicks[0] and not clicked: 
            self._mode = 0
            self._level = 1
            self._menu = False
            self._time_passed = 0
            self._total_shots = 0
            self._points = 0
            self._clicked = True
            self._new_coords = True
        if self.ammo_button.collidepoint(mouse_position) and self._clicks[0] and not clicked:
            self._mode = 1
            self._level = 1
            self._menu = False
            self._time_passed = 0
            self._ammo = 81
            self._total_shots = 0
            self._points = 0
            self._clicked = True
            self._new_coords = True
        if self.timed_button.collidepoint(mouse_position) and self._clicks[0] and not clicked:
            self._mode = 2
            self._level = 1
            self._menu = False
            self._time_remaining = 30
            self._time_passed = 0
            self._total_shots = 0
            self._points = 0
            self._clicked = True
            self._new_coords = True
        if self.reset_button.collidepoint(mouse_position) and self._clicks[0] and not clicked:
            self._best_freeplay = 0
            self._best_ammo = 0
            self._best_timed = 0
            self._write_values = True
            self._clicked = True

    def draw_buttons(self):
        self.ammo_button = pygame.rect.Rect((475, 524), (260, 100))
        self.timed_button = pygame.rect.Rect((170, 661), (260, 100))
        self.freeplay_button = pygame.rect.Rect((170, 524), (260, 100))
        self.reset_button = pygame.rect.Rect((475, 661), (260, 100))
