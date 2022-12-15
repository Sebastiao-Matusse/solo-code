import pygame
import math
# Contants & Global Variables

fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font("arcade/assets/font/myFont.ttf", 32)
big_font = pygame.font.Font("arcade/assets/font/myFont.ttf", 60)
menu_img = pygame.image.load(f"arcade/assets/menus/mainMenu.png")
game_over_img = pygame.image.load(f"arcade/assets/menus/gameOver.png")
pause_img = pygame.image.load(f"arcade/assets/menus/pause.png")

WIDTH = 900
HEIGHT = 800
lasers = ["red", "purple", "green"]
gun_point = (WIDTH/2, HEIGHT - 200)
bgs = []
banners = []
guns = []
target_images = [[], [], []]
target_boxes = [[], [], []]
targets = {
    1: [10, 5, 3],
    2: [12, 8, 5],
    3: [15, 12, 8, 3]}
level = 0
points = 0
shot = False
total_shots = 0
counter = 1
best_freeplay = 0
best_ammo = 0
best_timed = 0
# 0 = freeplay, 1 = accuracy, 2 = timed
mode = 0
ammo = 0
time_passed = 0
time_remaining = 0
clicked = False
write_values = False
menu = True
new_coords = True
one_coords = [[], [], []]
two_coords = [[], [], []]
three_coords = [[], [], [], []]

run = False
pause = False
screen = pygame.display.set_mode([WIDTH, HEIGHT])
mouse_position = pygame.mouse.get_pos()
clicks = pygame.mouse.get_pressed()
exit_button = pygame.rect.Rect((170, 661), (260, 100))
menu_button = pygame.rect.Rect((475, 661), (260, 100))
