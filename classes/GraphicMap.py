import classes.Space as Space

class GraphicMap:
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    @property
    def spacing_cross(self):
        return self.__spacing_cross

    @spacing_cross.setter
    def spacing_cross(self, spacing):
        self.__spacing_cross = spacing

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def margin_x(self):
        return self.__margin_x

    @margin_x.setter
    def margin_x(self, margin_x):
        self.__margin_x = margin_x

    @property
    def margin_y(self):
        return self.__margin_y

    @margin_y.setter
    def margin_y(self, margin_y):
        self.__margin_y = margin_y

    def __init__(self, size, spacing_cross, limit):
        self.__size = size
        self.__spacing_cross = spacing_cross
        self.__width = limit.x * spacing_cross
        self.__height = limit.y * spacing_cross
        self.__margin_x = (size[0] - ((limit.x + 1) * spacing_cross)) / 2
        self.__margin_y = (size[1] - ((limit.y + 1) * spacing_cross)) / 2

    def generate_line_bar(self, limit):
        """
        create list start, end of line bar
        :return: list pixel
        """
        lines = []
        for i in range(limit.y + 2):
            lines.append(((0 + self.margin_x, i * self.spacing_cross + self.margin_y),
                          (self.size[0] - self.margin_x, i * self.spacing_cross + self.margin_y)))
        return lines

    def generate_cross_bar(self, limit):
        """
        create list start, end of line bar
        :return: list position
        """
        crosses = []
        for i in range(limit.x + 2):
            crosses.append(((i * self.spacing_cross + self.margin_x, 0 + self.margin_y),
                            (i * self.spacing_cross + self.margin_x, self.size[1] - self.margin_y)))
        return crosses


def convert_position_to_pixel(graph, position):
    x = position.x * graph.spacing_cross + graph.margin_x
    y = graph.size[1] - position.y * graph.spacing_cross - graph.margin_y - graph.spacing_cross
    return x, y
