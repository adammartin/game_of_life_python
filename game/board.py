import numpy as np

class Board(object):
  def __init__(self, initial_matrix, rules):
    self.__matrix = np.array(initial_matrix)
    self.__rules = rules

  def next_board(self):
    return self.__populate_board(np.zeros_like(self.__matrix))

  def __populate_board(self, next_board):
    it = np.nditer(self.__matrix, flags=['multi_index'])
    for x in it:
      next_board[it.multi_index] = self.__rules.apply(it.multi_index, self.__matrix)
    return next_board.tolist()
