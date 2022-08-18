import pygame
import os
import time

width, height = 1920, 1080
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (width - 350, height - 500)
screen = pygame.display.set_mode((300, 400), pygame.NOFRAME)

while 1:
    screen = pygame.display.set_mode((200, 400), pygame.NOFRAME)
    pygame.display.update()
    pygame.event.pump()
    time.sleep(1)
    screen = pygame.display.set_mode((300, 400), pygame.NOFRAME)
    pygame.display.update()
    pygame.event.pump()
    time.sleep(1)
