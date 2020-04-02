import unittest
from unittest.mock import MagicMock

from social_distancing_sim.population.population import Population


class TestPopulation(unittest.TestCase):
    _sut = Population
    _mock_observation_space = MagicMock()
    _mock_healthcare = MagicMock()
    _mock_disease = MagicMock()

    def test_init_with_defaults(self):
        pop = self._sut(disease=self._mock_disease,
                        healthcare=self._mock_healthcare,
                        observation_space=self._mock_observation_space)

        self.assertIsInstance(pop, Population)
