import pygame
import math

GREY = 128, 128, 128
BLACK = 0, 0, 0
GREEN = 3, 160, 98
WHITE = 255, 255, 255
pygame.init()


def fill_dot(color, position):
    """
    Fill dot with color
    :param color: foreground color
    :param position: dot position
    :return: void
    """
    start_x = position[0] * SPACING_CROSS + MARGIN
    start_y = SIZE[1] - position[1] * SPACING_CROSS - MARGIN - SPACING_CROSS
    pygame.draw.rect(SCREEN, color, pygame.Rect(start_x, start_y, SPACING_CROSS, SPACING_CROSS))


def fill_map_border():
    """
    fill border of map
    :return: void
    """
    max_x = (SIZE[0] - MARGIN * 2) // SPACING_CROSS
    max_y = (SIZE[1] - MARGIN * 2) // SPACING_CROSS
    for i in range(max_x):
        fill_dot(GREY, (i, 0))
        fill_dot(GREY, (i, max_y - 1))
    for j in range(1, max_y - 1):
        fill_dot(GREY, (0, j))
        fill_dot(GREY, (max_x - 1, j))


def fill_polygon(points, color):
    """
    fill polygon with points
    :param color: color of dot
    :param points: list of point
    :return: void
    """
    # border is 50% transparency of color param
    global m
    opacity = 0.5
    border_color = opacity * color[0] + (1 - opacity) * 255, \
                   opacity * color[1] + (1 - opacity) * 255, \
                   opacity * color[2] + (1 - opacity) * 255
    # draw points
    for point in points:
        fill_dot(color, point)
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
            fill_dot(border_color, (pos_x, pos_y))


def print_text(content, pos):
    font = pygame.font.Font('Vera.ttf', 12)
    text = font.render(content, True, BLACK, None)
    textRect = text.get_rect()
    textRect.center = pos
    SCREEN.blit(text, textRect)


def indexing():
    max_x = (SIZE[0] - MARGIN * 2) // SPACING_CROSS
    max_y = (SIZE[1] - MARGIN * 2) // SPACING_CROSS
    for i in range(max_x):
        print_text(str(i), ((i * SPACING_CROSS) + MARGIN + SPACING_CROSS // 2, SIZE[1] - MARGIN // 2))
    for j in range(max_y):
        print_text(str(max_y - j - 1), ((MARGIN // 2), (j * SPACING_CROSS) + MARGIN + SPACING_CROSS // 2))


def draw_mesh(color):
    """
    draw mesh
    :return: void
    """
    # Draw border of grid
    # top
    pygame.draw.line(SCREEN, color, (0 + MARGIN, 0 + MARGIN), (SIZE[0] - MARGIN, 0 + MARGIN), 2)
    # right
    pygame.draw.line(SCREEN, color, (SIZE[0] - MARGIN, 0 + MARGIN), (SIZE[0] - MARGIN, SIZE[1] - MARGIN), 2)
    # bottom
    pygame.draw.line(SCREEN, color, (SIZE[0] - MARGIN, SIZE[1] - MARGIN), (0 + MARGIN, SIZE[1] - MARGIN), 2)
    # left
    pygame.draw.line(SCREEN, color, (0 + MARGIN, 0 + MARGIN), (0 + MARGIN, SIZE[1] - MARGIN), 2)
    # Draw line bar
    for i in range(1, (SIZE[1] - MARGIN * 2) // SPACING_CROSS):
        pygame.draw.line(SCREEN, color, (0 + MARGIN, i * SPACING_CROSS + MARGIN),
                         (SIZE[0] - MARGIN, i * SPACING_CROSS + MARGIN), 1)
    # Draw cross bar
    for j in range(1, (SIZE[0] - MARGIN * 2) // SPACING_CROSS):
        pygame.draw.line(SCREEN, color, (j * SPACING_CROSS + MARGIN, 0 + MARGIN),
                         (j * SPACING_CROSS + MARGIN, SIZE[1] - MARGIN), 1)


def draw_window(background):
    """
    Draw static elements
    :param background: color of background
    :return:
    """
    # example polygons
    points = [(4, 4), (5, 9), (8, 10), (9, 5)]
    triangle = [(8, 12), (8, 17), (13, 12)]
    rectangle = [(11, 1), (11, 6), (14, 6), (14, 1)]
    # change background
    SCREEN.fill(background)
    fill_polygon(points, GREEN)
    fill_polygon(triangle, GREEN)
    fill_polygon(rectangle, GREEN)
    fill_map_border()
    draw_mesh(BLACK)


def graphic_init(screen, size, margin, spacing_cross):
    global SIZE
    global MARGIN
    global SPACING_CROSS
    global SCREEN

    SIZE = size
    MARGIN = margin
    SPACING_CROSS = spacing_cross
    SCREEN = screen

    draw_window(WHITE)
    indexing()
