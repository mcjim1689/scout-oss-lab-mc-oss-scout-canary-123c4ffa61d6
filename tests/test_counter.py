import unittest

from counter import format_count


class CounterTests(unittest.TestCase):
    def test_zero_and_multiple_records(self):
        self.assertEqual(format_count(0), "0 records")
        self.assertEqual(format_count(3), "3 records")
