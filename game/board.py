import numpy as np

class Board(object):
  def __init__(self, initial_matrix, rules):
    self.matrix = np.array(initial_matrix)
    self.rules = rules

  def populate_board(self, next_board):
    it = np.nditer(self.matrix, flags=['multi_index'])
    while not it.finished:
      next_board[it.multi_index] = self.rules.apply(it.multi_index, self.matrix)
      it.iternext()
    return next_board.tolist()

  def next_board(self):
    return self.populate_board(np.zeros_like(self.matrix))
