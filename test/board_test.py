import unittest
import nose.tools as nt
from unittest import mock
from game.board import Board
from game.rules import Rules

class BoardTest(unittest.TestCase):
  def setUp(self):
    self.size = 3
    self.life_rules = mock.create_autospec(Rules, spec_set=True, instance=True)
    self.board = Board(self.empty_matrix(self.size), self.life_rules)

  def test_can_construct_board_with_no_life(self):
    self.life_rules.apply.return_value = 0
    nt.assert_equal(self.board.next_board(), self.empty_matrix(self.size))

  def test_next_board_will_have_life_rules_applied(self):
    self.life_rules.apply.return_value = 1
    nt.assert_equal(self.board.next_board(), self.empty_matrix(self.size, 1))

  def empty_matrix(self, size, initial_value = 0):
    return [[initial_value for x in range(size)] for x in range(size)]
