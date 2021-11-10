import numpy as np
import libs.helper as hp
import classes.Space as Space


def create_matrix(size_matrix, obstacles):
    matrix = np.ones((size_matrix.x + 1, size_matrix.y + 1))
    for obstacle in obstacles:
        for point in obstacle:
            matrix[point.x, point.y] = -1
        for border in hp.get_border_of_polygon(obstacle):
            matrix[border.x, border.y] = -1
    return matrix


def is_valid(matrix, position):
    size = matrix.shape
    if position.x >= size[0] - 1 or position.x <= 0:
        return False
    if position.y >= size[1] - 1 or position.y <= 0:
        return False
    if matrix[position.x, position.y] == -1:
        return False
    return True


def action(matrix, current):
    nodes = []
    t = False
    r = False
    b = False
    l = False
    # Top
    top = Space.Position(current.x, current.y + 1)
    if is_valid(matrix, top):
        nodes.append(top)
        t = True
    # Right
    right = Space.Position(current.x + 1, current.y)
    if is_valid(matrix, right):
        nodes.append(right)
        r = True
    # Top-right
    top_right = Space.Position(current.x + 1, current.y + 1)
    if (t or r is True) and is_valid(matrix, top_right):
        nodes.append(top_right)
    # Bottom
    bottom = Space.Position(current.x, current.y - 1)
    if is_valid(matrix, bottom):
        nodes.append(bottom)
        b = True
    # Right-bottom
    right_bot = Space.Position(current.x + 1, current.y - 1)
    if (r or b is True) and is_valid(matrix, right_bot):
        nodes.append(right_bot)
    # Left
    left = Space.Position(current.x - 1, current.y)
    if is_valid(matrix, left):
        nodes.append(left)
        l = True
    # Left-bottom
    left_bot = Space.Position(current.x - 1, current.y - 1)
    if (l or b is True) and is_valid(matrix, left_bot):
        nodes.append(left_bot)
    # Left-top
    left_top = Space.Position(current.x - 1, current.y + 1)
    if (l or t is True) and is_valid(matrix, left_top):
        nodes.append(left_top)
    return nodes


def backtrace(solution, start, goal):
    if len(solution) == 0:
        return []
    path = [goal]
    while not path[-1].equal(start):
        # path.append(solution[path[-1]])
        for child, parent in solution.items():
            if child.equal(path[-1]):
                path.append(parent)
    path.reverse()
    return path


def bfs(graph, start, goal):
    frontier = []
    visited = []
    solution = {}
    frontier.append(start)

    if start.equal(goal):
        return []
    while frontier:
        node = frontier.pop(0)
        visited.append(node)
        for neighbour in action(graph, node):
            if neighbour.not_in(visited) and neighbour.not_in(frontier):
                if neighbour.equal(goal):
                    solution[neighbour] = node
                    return solution
                frontier.append(neighbour)
                solution[neighbour] = node
    return []


def dfs(graph, start, goal):
    frontier = []
    visited = []
    solution = {}
    frontier.append(start)

    if start.equal(goal):
        return []
    while frontier:
        node = frontier.pop()
        visited.append(node)
        for neighbour in action(graph, node):
            if neighbour.not_in(visited) and neighbour.not_in(frontier):
                if neighbour.equal(goal):
                    solution[neighbour] = node
                    return solution
                frontier.append(neighbour)
                solution[neighbour] = node
    return []
