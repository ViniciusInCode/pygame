import pygame as pg
from random import randrange

def get_random_position():
    return [randrange(*RANGE), randrange(*RANGE)]

WINDOW = 700
TITLE_SIZE = 30
RANGE = (TITLE_SIZE // 2, WINDOW - TITLE_SIZE)
screen = pg.display.set_mode((WINDOW,WINDOW))
pg.display.set_caption("Snake Game")
snake = pg.rect.Rect(0, 0, TITLE_SIZE - 2, TITLE_SIZE - 2)
snake.center = get_random_position()

snake_dir = (0, 0)
time, time_step = 0, 110

clock = pg.time.Clock();

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.KEYDOWN:
            if event_key == pg.K

    screen.fill("red")

    pg.draw

    pg.display.flip()
    clock.tick(60)