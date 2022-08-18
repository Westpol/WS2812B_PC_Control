import pygame
import time
import os
import win32gui
import win32con

width, height = 1920, 1080
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 50)
screen = pygame.display.set_mode((1, 200), pygame.NOFRAME)
hwnd = win32gui.GetForegroundWindow()
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 50, 0, 0, win32con.SWP_NOSIZE)

screen.fill((255, 255, 255))
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
            screen.fill((255, 255, 255))
            pygame.display.update()
            if int((time.time() - startTime) * 1000) >= 250:
                break
        screen = pygame.display.set_mode((250, 200), pygame.NOFRAME)
        screen.fill((255, 255, 255))
        hwnd = win32gui.GetForegroundWindow()
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 50, 0, 0, win32con.SWP_NOSIZE)
        pygame.display.update()
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEWE)
        while 1:
            screen = pygame.display.set_mode((250 - int((time.time() - startTime) * 1000), 200), pygame.NOFRAME)
            screen.fill((255, 255, 255))
            pygame.display.update()
            if 250 - int((time.time() - startTime) * 1000) <= 1:
                break
        screen = pygame.display.set_mode((1, 200), pygame.NOFRAME)
        screen.fill((255, 255, 255))
        hwnd = win32gui.GetForegroundWindow()
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 50, 0, 0, win32con.SWP_NOSIZE)
        pygame.display.update()
    windowState = not windowState


while 1:
    pygame.event.pump()
    if pygame.mouse.get_pressed(3)[0]:
        expandWindow()
    pygame.event.pump()
