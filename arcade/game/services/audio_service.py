import pygame

pygame.mixer.music.load("arcade/assets/sounds/bg_music.mp3")
plate_sound = pygame.mixer.Sound("arcade/assets/sounds/Broken plates.wav")
plate_sound.set_volume(.4)
bird_sound = pygame.mixer.Sound("arcade/assets/sounds/Drill Gear.mp3")
bird_sound.set_volume(.4)
laser_sound = pygame.mixer.Sound("arcade/assets/sounds/Laser Gun.wav")
laser_sound.set_volume(.5)
pygame.mixer.music.play()
