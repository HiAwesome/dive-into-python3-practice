import unittest
import p272_roman2 as roman


class ToRomanBadInput(unittest.TestCase):
    def test_too_large(self):
        """to_roman should fail with large input"""
        self.assertRaises(roman.OutOfRangeErrer, roman.to_roman, 4000)
