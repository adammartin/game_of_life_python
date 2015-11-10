import numpy as np
from game.life_counter import LifeCounter

class Rules(object):
  def __init__(self, life_counter):
    self.life_counter = life_counter

  def apply(self, index, matrix):
    alive = matrix[index]
    living_neighbors = self.life_counter.count(index, matrix)
    return self.__living_cell_check(living_neighbors) if alive else self.__dead_cell_check(living_neighbors)

  def __living_cell_check(self, living_neighbors):
    if 2 <= living_neighbors <= 3:
      return 1
    return 0

  def __dead_cell_check(self, living_neighbors):
    return 1 if living_neighbors == 3 else 0
