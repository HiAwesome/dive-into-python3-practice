import unittest


class ToRomanBadInput(unittest.TestCase):
    def test_too_large(self):
        """to_roman should fail with large input"""
        self.assertRaises(roman2.OutOfRangeErrer, roman2.to_roman, 4000)
