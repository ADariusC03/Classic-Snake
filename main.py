"""
Classical Snake Game
Created By : A'Darius Craig
Nov. ,2020
"""

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

pygame.init()

# Title and Icon
pygame.display.set_caption("Classic Snake")
icon = pygame.image.load("snakes.png")
pygame.display.set_icon(icon)




class cube(object):
    rows = 20
    w = 500

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass


class snake(object):
    def __init__(self, color, pos):
        pass

    def move(self):
        pass

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        pass


def drawGrid(w, rows, surface):
    sizeBtwn = w // rows

    x = 0
    y = 0
    for i in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


def redrawWindow(surface):
    global rows, width
    surface.fill((0, 0, 0))  # Fills the screen with black
    drawGrid(width, rows, surface)  # Draw grid lines
    pygame.display.update()  # Updates the screen


def randomSnack(rows, item):
    pass


def message_box(subject, content):
    pass


def main():
    global width, rows, s

    width = 500
    height = 500
    rows = 20

    win = pygame.display.set_mode((width, height))  # Creates the screen object

    s = snake((0, 255, 0), (10, 10))

    clock = pygame.time.Clock()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.time.delay(40)  # Delay the game so it doesn't run quickly lower = faster

        clock.tick(20)  # Makes sure games run at 10 FPS. lower = slower
        redrawWindow(win)  # Will refresh the screen


main()
