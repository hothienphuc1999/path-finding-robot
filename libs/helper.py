import classes.Space as Space


def get_border_of_polygon(positions):
    """
    get points of border of polygon
    :param positions: list of point
    :return: list points
    """
    # append first point to list order to draw border of polygon
    data = []
    positions.append(positions[0])
    for i in range(len(positions) - 1):
        point_a = Space.Position(positions[i].x, positions[i].y)
        point_b = Space.Position(positions[i + 1].x, positions[i + 1].y)
        # find length of two point
        length = point_a.distance(point_b)

        # draw points on the line between two points
        for j in range(1, length):
            deltaX = (point_b.x - point_a.x)
            deltaY = (point_b.y - point_a.y)
            pos_x = round(point_a.x + j * ((point_b.x - point_a.x) / int(length)))
            if deltaX == 0:
                if point_a.y < point_b.y:
                    pos_y = point_a.y + j
                else:
                    pos_y = point_a.y - j
            else:
                m = deltaY / deltaX
                pos_y = round(m * (j * (deltaX / int(length))) + point_a.y)
            data.append(Space.Position(pos_x, pos_y))
    return data
