import numpy as np
import unittest
import nose.tools as nt
from unittest import mock
from game.life_counter import LifeCounter

class LifeCounterTest(unittest.TestCase):
  def setUp(self):
    self.board = np.zeros((3,3))
    self.life_counter = LifeCounter();

  def test_can_detect_no_living_neighbors(self):
    nt.assert_equal(self.life_counter.count((1,1), self.board), 0)

  def test_cell_does_not_count_itself_as_living_neighbor(self):
    self.board[(1,1)]=1
    nt.assert_equal(self.life_counter.count((1,1), self.board), 0)

  def test_can_detect_one_living_neighbor(self):
    self.board[(0,1)]=1
    nt.assert_equal(self.life_counter.count((1,1), self.board), 1)

  def test_when_dealing_with_upper_left_corner_counts_correctly(self):
    self.board[(2,0)]=1
    self.board[(0,2)]=1
    nt.assert_equal(self.life_counter.count((0,0), self.board), 0)

  def test_can_detect_when_all_life_is_alive_around_central_point(self):
    board = np.full((3,3), 1.0)
    nt.assert_equal(self.life_counter.count((1,1), board), 8)
