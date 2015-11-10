import unittest
import nose.tools as nt
import numpy as np
from unittest import mock
from game.life_counter import LifeCounter
from game.rules import Rules

class RulesTest(unittest.TestCase):
  def setUp(self):
    self.matrix = np.zeros((3,3))
    self.index = (1,1)
    self.matrix[self.index] = 1
    self.mock_life = mock.create_autospec(LifeCounter, spec_set=True, instance=True)
    self.rules = Rules(self.mock_life)

  def test_if_alive_will_return_death_for_less_than_2_living_neighbors(self):
    self.mock_life.count.return_value = 1.0
    nt.assert_equals(self.rules.apply(self.index, self.matrix), 0)

  def test_if_alive_will_return_life_for_2_living_neighbors(self):
    self.mock_life.count.return_value = 2.0
    nt.assert_equals(self.rules.apply(self.index, self.matrix), 1)

  def test_if_alive_will_return_life_for_3_living_neighbors(self):
    self.mock_life.count.return_value = 3.0
    nt.assert_equals(self.rules.apply(self.index, self.matrix), 1)

  def test_if_alive_will_return_death_for_4_living_neighbors(self):
    self.mock_life.count.return_value = 4.0
    nt.assert_equals(self.rules.apply(self.index, self.matrix), 0)

  def test_if_dead_will_return_dead_for_2_living_neighbors(self):
    self.matrix[self.index] = 0
    self.mock_life.count.return_value = 2.0
    nt.assert_equals(self.rules.apply(self.index, self.matrix), 0)

  def test_if_dead_but_has_3_living_neighbors_then_comes_alive(self):
    self.matrix[self.index] = 0
    self.mock_life.count.return_value = 3.0
    nt.assert_equals(self.rules.apply(self.index, self.matrix), 1)
