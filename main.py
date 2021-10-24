# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# Errors: Missing index, wrong Oxy
import sys
import pygame
import helpers.graphic as graphic

SIZE = width, height = 1440, 720
SPEED = [2, 2]
MARGIN = 40
SPACING_CROSS = 20
SCREEN = pygame.display.set_mode(SIZE)
FPS = 60
pygame.display.set_caption('Robot Tìm Đường')
# ball
BALL_WIDTH, BALL_HEIGHT = 75, 75
BALL_IMAGE = pygame.image.load('assets/intro_ball.gif')
BALL_SCALED = pygame.transform.scale(BALL_IMAGE, (BALL_WIDTH, BALL_HEIGHT))


def ball_movement(ball):
    if ball.left < 0 or ball.right > width:
        SPEED[0] = -SPEED[0]
    if ball.top < 0 or ball.bottom > height:
        SPEED[1] = -SPEED[1]

    ball.x += SPEED[0]
    ball.y += SPEED[1]


def run_game():
    clock = pygame.time.Clock()
    ball = pygame.Rect(0, 0, BALL_WIDTH, BALL_HEIGHT)

    while 1:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        graphic.graphic_init(SCREEN, SIZE, MARGIN, SPACING_CROSS)
        pygame.display.update()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
