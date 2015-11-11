

class LifeCounter(object):
    def count(self, cell, matrix):
        return self.__subset(cell, matrix).sum() - matrix[cell]

    def __subset(self, cell, matrix):
        lower_x = self.__lower_bound(cell[0])
        lower_y = self.__lower_bound(cell[1])
        upper_x = self.__upper_bound(lower_x, cell[0], matrix.shape[0])
        upper_y = self.__upper_bound(lower_y, cell[1], matrix.shape[1])
        return matrix[lower_x:upper_x, lower_y:upper_y]

    def __upper_bound(self, lower_bound, base, absolute_max):
        max_pos = self.__max_pos(base, lower_bound)
        return min(lower_bound+max_pos, absolute_max)

    def __lower_bound(self, base):
        return max(base-1, 0)

    def __max_pos(self, base, lower_bound):
        return base - lower_bound + 2
