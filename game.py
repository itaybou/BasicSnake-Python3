import config
import pygame
import random
import tkinter as tk
from tkinter import messagebox


def drawGrid(width, rows, surface):
    size = width // rows  # Integer division

    x = 0
    y = 0
    for row in range(rows):
        x += size
        y += size
        pygame.draw.line(surface, (0, 0, 0), (x, 0), (x, width))
        pygame.draw.line(surface, (0, 0, 0), (0, y), (width, y))


def redrawWindow(surface, snake, food):
    surface.fill((0, 0, 0))
    snake.draw(surface)
    food.draw(surface)
    drawGrid(config.width, config.rows, surface)
    pygame.display.update()


def message(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destory()
    except:
        pass


def randomFood(snake):
    snake_positions = snake.body
    while True:
        randX = random.randrange(config.rows)
        randY = random.randrange(config.rows)
        if len(list(filter(lambda z: z.pos == (randX, randY), snake_positions))) > 0:
            continue
        else:
            break

    return (randX, randY)
