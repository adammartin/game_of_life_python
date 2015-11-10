import numpy as np
from game.life_counter import LifeCounter

class Rules(object):
  def __init__(self, life_counter):
    self.__life_counter = life_counter

  def apply(self, index, matrix):
    alive = matrix[index]
    living_neighbors = self.__life_counter.count(index, matrix)
    if (living_neighbors==2 and alive) or (living_neighbors == 3):
      return 1
    return 0
