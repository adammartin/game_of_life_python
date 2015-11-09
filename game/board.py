import numpy as np

class Board(object):
  def __init__(self, initial_matrix, rules):
    self.matrix = np.array(initial_matrix)
    self.rules = rules

  def next_board(self):
    next_board = np.zeros_like(self.matrix)
    it = np.nditer(self.matrix, flags=['multi_index'])
    while not it.finished:
      new_val = self.rules.apply(it.multi_index, self.matrix)
      next_board[it.multi_index] = new_val
      it.iternext()
    return next_board.tolist()
