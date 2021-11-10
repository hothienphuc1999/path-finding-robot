# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pygame
import pygame_menu
import libs.graphic as graphic
import algorithms.path_finding as al
import classes.Space as Space

SIZE = (1080, 720)
SPACING_CROSS = 30
MARGIN_MIN = 20
SCREEN = pygame.display.set_mode(SIZE)
FPS = 60
pygame.display.set_caption('Robot Tìm Đường')
ALGORYTHMS = 0


def draw_graphic(solution):
    clock = pygame.time.Clock()
    while 1:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    draw_menu()
        graphic.graphic_init(SCREEN, SIZE, SPACING_CROSS, SPACE, START, GOAL, solution)
        pygame.display.update()


def set_algorythms(value, algs: int):
    global ALGORYTHMS
    ALGORYTHMS = algs


def start_the_game():
    solution = []
    limit = Space.Position(SPACE.max_x, SPACE.max_y)
    if ALGORYTHMS == 0:
        return
    if ALGORYTHMS == 1:
        solution = al.bfs(al.create_matrix(limit, SPACE.obstacle), START, GOAL)
    if ALGORYTHMS == 2:
        solution = al.dfs(al.create_matrix(limit, SPACE.obstacle), START, GOAL)
    draw_graphic(solution)


def draw_menu():
    menu = pygame_menu.Menu('Main Menu', SIZE[0], SIZE[1],
                            theme=pygame_menu.themes.THEME_BLUE)
    menu.add.button('Go', start_the_game)
    menu.add.selector('Algorithms :',
                      [('Choose', 0),
                       ('Breath-First Search', 1),
                       ('Depth-First Search', 2)],
                      onchange=set_algorythms)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(SCREEN)


# Press the green button in the gutter to run the script.
def load_data():
    global SPACE
    global START
    global GOAL
    f = open("data.txt", "r")
    # Line 1: Coordinate limit
    row = f.readline()
    data = row.split(",")
    limit = Space.Position(int(data[0]), int(data[1]))
    # Line 2: Start, Goal and list Pickup list position
    row = f.readline()
    data = row.split(",")

    START = Space.Position(int(data.pop(0)), int(data.pop(0)))
    GOAL = Space.Position(int(data.pop(0)), int(data.pop(0)))
    # Line 3: Number of obstacles
    # Line 4,...: Position of obstacles
    obstacles = []
    for i in range(int(f.readline())):
        row = f.readline()
        data = row.split(",")
        ob = []
        while data:
            ob.append(Space.Position(int(data.pop(0)), int(data.pop(0))))
        obstacles.append(ob)
    SPACE = Space.Space(limit.x, limit.y, obstacles)
    f.close()
    if ((SIZE[0] - MARGIN_MIN * 2) // SPACING_CROSS - 1 >= limit.x and
            (SIZE[1] - MARGIN_MIN * 2) // SPACING_CROSS - 1 >= limit.y):
        return 1
    return 0


if __name__ == '__main__':
    if load_data() == 1:
        draw_menu()
    else:
        max_x = (SIZE[0] - MARGIN_MIN * 2) // SPACING_CROSS - 1
        max_y = (SIZE[1] - MARGIN_MIN * 2) // SPACING_CROSS - 1
        print('Giới hạn không gian Oxy vượt quá phạm vi hiển thị của phần mềm.')
        print('Vui lòng điều chỉnh lại giới hạn không gian trong file data.txt với trục x không quá {0}'
              ', trục y không quá {1}'.format(max_x, max_y))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
