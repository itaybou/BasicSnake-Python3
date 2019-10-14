from lib.cube import cube
import pygame
import config


class snake(object):
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirx = 0
        self.diry = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirx = -1
                    self.diry = 0
                    self.turns[self.head.pos[:]] = [self.dirx, self.diry]

                elif keys[pygame.K_RIGHT]:
                    self.dirx = 1
                    self.diry = 0
                    self.turns[self.head.pos[:]] = [self.dirx, self.diry]

                elif keys[pygame.K_UP]:
                    self.dirx = 0
                    self.diry = -1
                    self.turns[self.head.pos[:]] = [self.dirx, self.diry]

                elif keys[pygame.K_DOWN]:
                    self.dirx = 0
                    self.diry = 1
                    self.turns[self.head.pos[:]] = [self.dirx, self.diry]

        for i, cube in enumerate(self.body):
            pos = cube.pos[:]
            if pos in self.turns:
                turn = self.turns[pos]
                cube.move(turn[0], turn[1])  # (x, y)
                if i == len(self.body) - 1:
                    self.turns.pop(pos)
            else:
                if cube.dirx == -1 and cube.pos[0] <= 0:
                    cube.pos = (config.rows-1, cube.pos[1])
                elif cube.dirx == 1 and cube.pos[0] >= config.rows-1:
                    cube.pos = (0, cube.pos[1])
                elif cube.diry == 1 and cube.pos[1] >= config.rows-1:
                    cube.pos = (cube.pos[0], 0)
                elif cube.diry == -1 and cube.pos[1] <= 0:
                    cube.pos = (cube.pos[0], config.rows-1)
                else:
                    cube.move(cube.dirx, cube.diry)

    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirx = 0
        self.diry = 1

    def eat(self):
        tail = self.body[-1]
        dx, dy = tail.dirx, tail.diry

        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0], tail.pos[1] + 1)))

        self.body[-1].dirx = dx
        self.body[-1].diry = dy

    def draw(self, surface):
        for i, cube in enumerate(self.body):
            if i == 0:
                cube.draw(surface, True)
            else:
                cube.draw(surface)
