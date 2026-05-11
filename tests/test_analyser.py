import unittest
from analytics.analyser import SleepAnalyser


class TestAnalyser(unittest.TestCase):

    def setUp(self):
        self.sample = [
            {"GPA": "3.8", "sleep_hours": "7"},
            {"GPA": "2.5", "sleep_hours": "5"},
            {"GPA": "3.9", "sleep_hours": "8"},
            {"GPA": "1.8", "sleep_hours": "4"},
            {"GPA": "3.5", "sleep_hours": "6"},
        ]

    def test_result_is_not_empty(self):
        analyser = SleepAnalyser(self.sample)
        analyser.analyse()
        self.assertNotEqual(analyser.result, {})

    def test_total_students(self):
        analyser = SleepAnalyser(self.sample)
        analyser.analyse()
        self.assertEqual(analyser.result["total_students"], 5)

    def test_result_has_required_keys(self):
        analyser = SleepAnalyser(self.sample)
        analyser.analyse()
        self.assertIn("low_sleep", analyser.result)
        self.assertIn("high_sleep", analyser.result)
        self.assertIn("gpa_difference", analyser.result)

    def test_analyse_twice(self):
        analyser = SleepAnalyser(self.sample)
        analyser.analyse()
        result1 = analyser.result.copy()
        analyser.analyse()
        self.assertEqual(analyser.result, result1)


if __name__ == "__main__":
    unittest.main()
