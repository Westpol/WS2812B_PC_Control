import pygame
import time
import os

backgroundColour = (100, 150, 255)
expandedSize = 250

width, height = 1920, 1080
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 50)
screen = pygame.display.set_mode((1, 200), pygame.NOFRAME)

screen.fill(backgroundColour)
pygame.display.update()
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEWE)

windowState = False     # False = collapsed, True = expanded


def expandWindow():
    global windowState, screen
    startTime = time.time()
    if not windowState:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        while 1:
            screen = pygame.display.set_mode((int((time.time() - startTime) * 1000), 200), pygame.NOFRAME)
            screen.fill(backgroundColour)
            pygame.display.update()
            if int((time.time() - startTime) * 1000) >= expandedSize:
                break
        screen = pygame.display.set_mode((expandedSize, 200), pygame.NOFRAME)
        screen.fill(backgroundColour)
        pygame.display.update()
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEWE)
        while 1:
            screen = pygame.display.set_mode((expandedSize - int((time.time() - startTime) * 1000), 200), pygame.NOFRAME)
            screen.fill(backgroundColour)
            pygame.display.update()
            if expandedSize - int((time.time() - startTime) * 1000) <= 1:
                break
        screen = pygame.display.set_mode((1, 200), pygame.NOFRAME)
        screen.fill(backgroundColour)
        pygame.display.update()
    windowState = not windowState


while 1:
    pygame.event.pump()
    if pygame.mouse.get_pressed(3)[0] and not windowState:
        expandWindow()
    elif pygame.mouse.get_pressed(3)[0] and windowState and expandedSize - 20 < pygame.mouse.get_pos()[0] < expandedSize:
        expandWindow()

    if windowState:
        pygame.draw.rect(screen, (255, 50, 50), (expandedSize - 20, 0, expandedSize, 200))
        pygame.draw.polygon(screen, (255, 255, 255), ((expandedSize - 15, 100), (expandedSize - 5, 95), (expandedSize - 5, 105)))
        pygame.display.flip()
    pygame.event.pump()
