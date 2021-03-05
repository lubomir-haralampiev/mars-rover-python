import unittest
from mars_rover.validation import validation


class ValidationTestCase(unittest.TestCase):
    def test_ensure_has_odd_lentgh_raises(self):
        """should raise ValueError"""
        with self.assertRaises(ValueError):
            validation.ensure_has_odd_lentgh([1, 2])

    def test_ensure_has_odd_lentgh_not_raises(self):
        """should not raise an Exception"""
        try:
            validation.ensure_has_odd_lentgh([1, 2, 3])
        except Exception:
            self.fail("ensure_has_odd_lentgh raised an Exception")
