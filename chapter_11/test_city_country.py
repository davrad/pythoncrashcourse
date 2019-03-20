import unittest
from city_country import format_city as fc

class CityCountryTest(unittest.TestCase):

    def test_correct_output_1(self):
        result = fc('New York','United States')
        self.assertEqual('New York, United States', result)

    def test_correct_output_2(self):
        result = fc('Sydney','Australia')
        self.assertEqual('Sydney, Australia', result)

    def test_correct_output_3(self):
        result = fc('Kinshasa','DR Congo')
        self.assertEqual('Kinshasa, DR Congo', result)

    def test_correct_output_population(self):
        result = fc('Nairobi','Kenia',int(4e6))
        self.assertEqual('Nairobi, Kenia - population 4000000',result)

    def test_correct_output_population_2(self):
        result = fc('Moscow','Russia',12500000)
        self.assertEqual('Moscow, Russia - population 12500000',result)

unittest.main()