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

    def __init__(self, start, dirnx=1, dirny=0, color=(0, 255, 0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos(self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows  # Width/Height of each cube
        i = self.pos[0]  # Current row
        j = self.pos[1]  # Current column

        # By multiplying the row and column value of our cube by the width
        # and height of each cube we can determine where to draw it
        pygame.draw.rect(surface, self.color, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))
        if eyes:  # Draws the eyes
            centre = dis // 2
            radius = 3
            circleMiddle = (i * dis + centre - radius, j * dis + 8)
            circleMiddle2 = (i * dis + dis - radius * 2, j * dis + 8)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)


class snake(object):
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)  # Front head of the snake given a specific position
        self.body.append(self.head)  # (cube object) Will add head

        # Keeps track of the direction you move in
        self.dirnx = 0  # Direction of x for moving our snake (if either is equal to -1,0,1 the other is 0 since it
        self.dirny = 1  # Direction of y for moving our snake, can only move in one direction at the same time)

    def move(self):
        keys = pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_LEFT]:  # makes x negative to move left
                self.dirnx = -1
                self.dirny = 0
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            elif keys[pygame.K_RIGHT]:  # make x positive to move right
                self.dirnx = 1
                self.dirny = 0
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            elif keys[pygame.K_UP]:
                self.dirnx = 0
                self.dirny = -1
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            elif keys[pygame.K_DOWN]:
                self.dirnx = 0
                self.dirny = 1
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                if c.dirnx == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows - 1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows - 1:
                    c.pos = (0, c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows - 1:
                    c.pos = (c.pos[0], c.row - 1)
                else:
                    c.move(c.dirnx, c.dirny)

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)


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
    global rows, width, s
    surface.fill((0, 0, 0))  # Fills the screen with black
    s.draw(surface)
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

    win = pygame.display.set_mode((width, width))  # Creates the screen object

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
