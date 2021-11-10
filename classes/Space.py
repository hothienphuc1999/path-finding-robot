import math


class Position:
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    def __int__(self):
        self.__x = 0
        self.__y = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def equal(self, position):
        if self.x == position.x and self.y == position.y:
            return True
        return False

    def not_in(self, list):
        for element in list:
            if self.x == element.x and self.y == element.y:
                return False
        return True

    def distance(self, to):
        # find the equation of the line formed by the points
        # Equation is y - ya = m(x - xa); m = (yB - yA)/(xB - xA)
        # deltaX = xB - xA
        deltaX = to.x - self.x
        # deltaY = yB - yA
        deltaY = to.y - self.y
        if deltaX != 0:
            m = deltaY / deltaX
        # find length of two point
        return int(math.sqrt(deltaX ** 2 + deltaY ** 2))


class Space:
    @property
    def min_x(self):
        return self.__min_x

    @min_x.setter
    def min_x(self, x):
        self.__min_x = x

    @property
    def min_y(self):
        return self.__min_y

    @min_y.setter
    def min_y(self, y):
        self.__min_y = y

    @property
    def max_x(self):
        return self.__max_x

    @max_x.setter
    def max_x(self, x):
        self.__max_x = x

    @property
    def max_y(self):
        return self.__max_y

    @max_y.setter
    def max_y(self, y):
        self.__max_y = y

    @property
    def obstacle(self):
        return self.__obstacles

    @obstacle.setter
    def obstacle(self, obstacle):
        self.__obstacles = obstacle

    def __init__(self, max_x, max_y, obstacles):
        self.__min_x = 0
        self.__min_y = 0
        self.__max_x = max_x
        self.__max_y = max_y
        self.__obstacles = obstacles
