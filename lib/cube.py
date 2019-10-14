import config
import pygame


class cube(object):

    def __init__(self, start, dirx=1, diry=0, color=(255, 0, 0)):
        self.pos = start
        self.dirx = 1
        self.diry = 0
        self.color = color

    def move(self, dirx, diry):
        self.dirx = dirx
        self.diry = diry
        self.pos = (self.pos[0] + self.dirx, self.pos[1] + self.diry)

    def draw(self, surface, eyes=False):
        delta = config.width // config.rows
        i = self.pos[0]
        j = self.pos[1]
        pygame.draw.rect(surface, self.color,
                         (i*delta+1, j*delta*1, delta-2, delta-2))
        if eyes:
            center = delta // 2
            radius = 3
            circleMiddle = (i*delta+center-radius, j*delta+8)
            circleMiddle2 = (i*delta+delta-radius*2, j*delta+8)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)
