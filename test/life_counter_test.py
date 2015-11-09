import numpy as np
import unittest
import nose.tools as nt
from unittest import mock
from game.life_counter import LifeCounter

class LifeCounterTest(unittest.TestCase):
  def setUp(self):
    scale = (3,3)
    self.board = np.zeros(scale)
    self.full_board = np.full(scale, 1.0)
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
    nt.assert_equal(self.life_counter.count((1,1), self.full_board), 8)

  def test_can_detect_all_life_around_upper_left_corner(self):
    nt.assert_equal(self.life_counter.count((0,0), self.full_board), 3)

  def test_can_detect_all_life_around_upper_right_corner(self):
    nt.assert_equal(self.life_counter.count((2,0), self.full_board), 3)

  def test_can_detect_all_life_around_lower_right_corner(self):
    nt.assert_equal(self.life_counter.count((2,2), self.full_board), 3)

  def test_can_detect_all_life_around_lower_left_corner(self):
    nt.assert_equal(self.life_counter.count((0,2), self.full_board), 3)

  def test_can_detect_all_life_around_middle_upper_edge(self):
    nt.assert_equal(self.life_counter.count((1,0), self.full_board), 5)

  def test_can_detect_all_life_around_middle_lower_edge(self):
    nt.assert_equal(self.life_counter.count((1,2), self.full_board), 5)
