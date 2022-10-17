import unittest
from city_function import get_city_country


class TestCityFunc(unittest.TestCase):
    def test_city_country(self):
        self.assertEqual(get_city_country('santiago', 'chile'), 'Santiago, Chile')

    def test_population(self):
        self.assertEqual(get_city_country('santiago', 'chile', 500), 'Santiago, Chile - population = 500')


if __name__ == '__main__':
    unittest.main()
