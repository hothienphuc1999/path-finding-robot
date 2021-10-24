# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# Errors: Missing index, wrong Oxy
import sys
import pygame
import math

SIZE = width, height = 720, 480
SPEED = [2, 2]
BLACK = 0, 0, 0
WHITE = 255, 255, 255
GREY = 128, 128, 128
MARGIN = 40
SPACING_CROSS = 20
BALL_WIDTH, BALL_HEIGHT = 75, 75
BALL_IMAGE = pygame.image.load('Assets/intro_ball.gif')
BALL_SCALED = pygame.transform.scale(BALL_IMAGE, (BALL_WIDTH, BALL_HEIGHT))
SCREEN = pygame.display.set_mode(SIZE)
FPS = 60
pygame.display.set_caption('Robot Tìm Đường')
pygame.init()]


def ball_movement(ball):
    if ball.left < 0 or ball.right > width:
        SPEED[0] = -SPEED[0]
    if ball.top < 0 or ball.bottom > height:
        SPEED[1] = -SPEED[1]

    ball.x += SPEED[0]
    ball.y += SPEED[1]


def print_text(content, pos):
    font = pygame.font.Font('Vera.ttf', 12)
    text = font.render(content, True, BLACK, None)
    textRect = text.get_rect()
    textRect.center = pos
    SCREEN.blit(text, textRect)


def indexing():
    max_x = (width - MARGIN * 2) // SPACING_CROSS
    max_y = (height - MARGIN * 2) // SPACING_CROSS
    for i in range(max_x):
        print_text(str(i), ((i * SPACING_CROSS) + MARGIN + SPACING_CROSS // 2, height - MARGIN // 2))
    for j in range(max_y):
        print_text(str(max_y - j - 1), ((MARGIN // 2), (j * SPACING_CROSS) + MARGIN + SPACING_CROSS // 2))


def fill_dot(color, position):
    """
    Fill dot with color
    :param color: foreground color
    :param position: dot position
    :return: void
    """
    start_x = position[0] * SPACING_CROSS + MARGIN
    start_y = height - position[1] * SPACING_CROSS - MARGIN - SPACING_CROSS
    pygame.draw.rect(SCREEN, color, pygame.Rect(start_x, start_y, SPACING_CROSS, SPACING_CROSS))


def fill_polygon(points, color):
    """
    fill polygon with points
    :param color: color of dot
    :param points: list of point
    :return: void
    """
    # draw points
    for point in points:
        fill_dot(BLACK, point)
    # append first point to list order to draw border of polygon
    points.append(points[0])
    for i in range(len(points) - 1):
        # find the equation of the line formed by the points
        # Equation is y - ya = m(x - xa); m = (yB - yA)/(xB - xA)
        xA = points[i][0]
        xB = points[i + 1][0]
        yA = points[i][1]
        yB = points[i + 1][1]
        deltaX = xB - xA
        deltaY = yB - yA
        if deltaX != 0:
            m = deltaY / deltaX

        # find length of two point
        length = int(math.sqrt(deltaX ** 2 + deltaY ** 2))

        # draw points on the line between two points
        for j in range(1, length):
            pos_x = round(xA + j * ((xB - xA) / int(length)))
            if deltaX == 0:
                if yA < yB:
                    pos_y = yA + j
                else:
                    pos_y = yA - j
            else:
                pos_y = round(m * (j * ((xB - xA) / int(length))) + yA)
            fill_dot(GREY, (pos_x, pos_y))


def draw_mesh(margin, spacing):
    """
    draw mesh
    :param margin: space from border of mesh to window
    :param spacing: pitch of line bar or cross bar
    :return: void
    """
    # Draw border of grid
    # top
    pygame.draw.line(SCREEN, BLACK, (0 + margin, 0 + margin), (SIZE[0] - margin, 0 + margin), 2)
    # right
    pygame.draw.line(SCREEN, BLACK, (SIZE[0] - margin, 0 + margin), (SIZE[0] - margin, SIZE[1] - margin), 2)
    # bottom
    pygame.draw.line(SCREEN, BLACK, (SIZE[0] - margin, SIZE[1] - margin), (0 + margin, SIZE[1] - margin), 2)
    # left
    pygame.draw.line(SCREEN, BLACK, (0 + margin, 0 + margin), (0 + margin, SIZE[1] - margin), 2)
    # Draw line bar
    for i in range(1, (height - margin * 2) // spacing):
        pygame.draw.line(SCREEN, BLACK, (0 + margin, i * spacing + margin), (SIZE[0] - margin, i * spacing + margin), 1)
    # Draw cross bar
    for j in range(1, (width - margin * 2) // spacing):
        pygame.draw.line(SCREEN, BLACK, (j * spacing + margin, 0 + margin), (j * spacing + margin, SIZE[1] - margin), 1)


def draw_window(ball):
    """
    Draw static elements
    :param ball:
    :return:
    """
    points = [(4, 4), (5, 9), (8, 10), (9, 5)]
    triangle = [(8, 12), (8, 17), (13, 12)]
    rectangle = [(11, 1), (11, 6), (14, 6), (14, 1)]
    # change background
    SCREEN.fill(WHITE)
    SCREEN.blit(BALL_SCALED, (ball.x, ball.y))
    fill_polygon(points, BLACK)
    fill_polygon(triangle, BLACK)
    fill_polygon(rectangle, BLACK)
    fill_dot(BLACK, (0,0))
    draw_mesh(MARGIN, SPACING_CROSS)


def run_game():
    clock = pygame.time.Clock()
    ball = pygame.Rect(0, 0, BALL_WIDTH, BALL_HEIGHT)

    while 1:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        draw_window(ball)
        indexing()
        ball_movement(ball)
        pygame.display.update()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
