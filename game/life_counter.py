import numpy as np

class LifeCounter(object):
  def count(self, cell, matrix):
    return self.subset(cell, matrix).sum() - matrix[cell]

  def subset(self, cell, matrix):
    lower_x = self.lower_bound(cell[0])
    lower_y = self.lower_bound(cell[1])
    upper_x = self.upper_bound(lower_x, cell[0], matrix.shape[0])
    upper_y = self.upper_bound(lower_y, cell[1], matrix.shape[1])
    return matrix[lower_x:upper_x, lower_y:upper_y]

  def upper_bound(self, lower_bound, base, absolute_max):
    max_pos = self.max_pos(base, lower_bound)
    return min(lower_bound+max_pos, absolute_max)

  def lower_bound(self, base):
    return max(base-1, 0)

  def max_pos(self, base, lower_bound):
    return base - lower_bound + 2
