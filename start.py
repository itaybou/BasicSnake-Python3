import pygame
import game as game
import config
from lib.snake import snake
from lib.cube import cube


def main():
    pygame.init()
    config.init()
    window = pygame.display.set_mode((config.width, config.width))
    s = snake((255, 0, 0), (10, 10))
    food = cube(game.randomFood(s), color=(0, 255, 0))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)  # 10 FPS
        s.move()
        if s.body[0].pos == food.pos:
            s.eat()
            food = cube(game.randomFood(s), color=(0, 255, 0))
        for part in range(len(s.body)):
            if s.body[part].pos in list(map(lambda z: z.pos, s.body[part+1:])):
                score = len(s.body)
                lost_message = "Score is: %d\nPlay again." % (score)
                print('Score: ', score)
                game.message("YOU LOST!", lost_message)
                s.reset((10, 10))
                break
        game.redrawWindow(window, s, food)


if __name__ == "__main__":
    main()
