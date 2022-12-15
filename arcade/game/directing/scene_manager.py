from constants import *
class SceneManager():
    def __init__(self):
        self._level = level
        
    def draw_level(self, coords):
        if level == 1 or level == 2:
            target_rects = [[], [], []]
        else:
            target_rects = [[], [], [], []]
        for i in range (len(coords)):
            for j in range (len(coords[i])):
                target_rects[i].append(pygame.rect.Rect((coords[i][j][0] + 20, coords[i][j][1]),
                (60 - i * 12, 60 - i * 12)))
                screen.blit(target_images[level - 1][i], coords[i][j])
        return target_rects

    def move_level(self, coords):
        if level == 1 or level == 2:
            max_val = 3
        else:
            max_val = 4
        for i in range(max_val):
            for j in range(len(coords[i])):
                my_coords = coords[i][j]
                if my_coords[0] < - 150:
                    coords[i][j] = (WIDTH, my_coords[1])
                else:
                    coords[i][j] = (my_coords[0] - 2**i, my_coords[1])
        return coords
