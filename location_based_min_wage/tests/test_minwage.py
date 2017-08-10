import unittest
from location_based_min_wage import minwage


class TestLocationBasedMinWage(unittest.TestCase):

    def setUp(self):
        self.source = 'location_based_min_wage/wikilist.html'

    def test_get_hourly_minimum_wage_for_country(self):
        self.assertEqual(minwage.get_minimumwage(
            'India', source=self.source), '0.3'
        )
        self.assertEqual(minwage.get_minimumwage(
            'United States', source=self.source), '7.25'
        )

    def test_country_name_case_insensitivity(self):
        self.assertEqual(minwage.get_minimumwage(
            'UNITED kingdom', source=self.source), '10.13'
        )

    def test_invalid_country_name(self):
        with self.assertRaises(SystemExit) as se:
            minwage.get_minimumwage("Invalid Country", source=self.source)

        self.assertEqual(se.exception.code, 0)


if __name__ == '__main__':
    unittest.main() 
