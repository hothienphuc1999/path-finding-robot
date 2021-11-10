import pygame
import libs.helper as hp
import algorithms.path_finding as al
import classes.GraphicMap as Map
import classes.Space as Space

GREY = 128, 128, 128
BLACK = 0, 0, 0
GREEN = 3, 160, 98
WHITE = 255, 255, 255
RED = 255, 51, 51
YELLOW = 255, 228, 181
pygame.init()


def fill_dot(color, position):
    """
    Fill dot with color
    :param color: foreground color
    :param position: position
    :return: void
    """
    pixel = Map.convert_position_to_pixel(GRAPH, position)
    pygame.draw.rect(SCREEN, color, pygame.Rect(pixel[0], pixel[1], GRAPH.spacing_cross, GRAPH.spacing_cross))


def fill_map_border():
    """
    fill border of map
    :return: void
    """
    for i in range(SPACE.max_x + 1):
        fill_dot(GREY, Space.Position(i, 0))
        fill_dot(GREY, Space.Position(i, SPACE.max_y))
    for j in range(1, SPACE.max_y + 1):
        fill_dot(GREY, Space.Position(0, j))
        fill_dot(GREY, Space.Position(SPACE.max_x, j))


def fill_polygon(points, color):
    """
    fill polygon with points
    :param color: color of dot
    :param points: list of point
    :return: void
    """
    # border is 50% transparency of color param
    opacity = 0.5
    border_color = (opacity * color[0] + (1 - opacity) * 255,
                    opacity * color[1] + (1 - opacity) * 255,
                    opacity * color[2] + (1 - opacity) * 255)
    # draw points
    for point in points:
        fill_dot(color, point)
    # append first point to list order to draw border of polygon
    for p in hp.get_border_of_polygon(points):
        fill_dot(border_color, p)


def print_text(content, position):
    pixel = Map.convert_position_to_pixel(GRAPH, position)
    font = pygame.font.Font('Vera.ttf', 12)
    text = font.render(content, True, BLACK, None)
    textRect = text.get_rect()
    textRect.center = (pixel[0] + GRAPH.spacing_cross / 2, pixel[1] + GRAPH.spacing_cross / 2)
    SCREEN.blit(text, textRect)


def indexing():
    for i in range(SPACE.max_x + 1):
        print_text(str(i), Space.Position(i, -1))
    for j in range(SPACE.max_y + 1):
        print_text(str(SPACE.max_y - j), Space.Position(-1, SPACE.max_y - j))


def draw_mesh(color):
    """
    draw mesh
    :return: void
    """
    # Draw line bar
    limit = Space.Position(SPACE.max_x, SPACE.max_y)
    for line in GRAPH.generate_line_bar(limit):
        pygame.draw.line(SCREEN, color, line[0], line[1], 1)
    # Draw cross bar
    for cross in GRAPH.generate_cross_bar(limit):
        pygame.draw.line(SCREEN, color, cross[0], cross[1], 1)


def draw_obstacles(obstacles):
    for ob in obstacles:
        fill_polygon(ob, GREEN)


def fill_start_goal(start, goal):
    fill_dot(RED, start)
    fill_dot(RED, goal)
    print_text("S", start)
    print_text("G", goal)


def fill_pickup(pickup):
    for p in pickup:
        fill_dot(GREY, p)
        print_text("P", p)


def graphic_init(screen, size, spacing_cross, space, start, goal, solution):
    global SCREEN
    global GRAPH
    global SPACE

    SCREEN = screen
    SPACE = space
    GRAPH = Map.GraphicMap(size, spacing_cross, Space.Position(SPACE.max_x, SPACE.max_y))

    SCREEN.fill(WHITE)
    fill_map_border()
    draw_obstacles(SPACE.obstacle)
    fill_start_goal(start, goal)
    draw_solution(solution, start, goal)
    draw_mesh(BLACK)
    indexing()


def draw_solution(solution, start, goal):
    if len(solution) == 0:
        print_text('Path not found!', Space.Position(SPACE.max_x // 2, -2))
        return
    # Fill path
    trace_path = al.backtrace(solution, start, goal)
    for i in range(1, len(trace_path) - 1):
        fill_dot(YELLOW, trace_path[i])
    # Mark letter 'x' with point explored
    last_item = list(solution.keys())[-1]
    for point, parent in solution.items():
        if not point.equal(last_item):
            print_text('x', point)
