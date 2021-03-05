import unittest
from mars_rover import process_lines


class ProcessLinesTestCase(unittest.TestCase):
    def test_empty_array_raises(self):
        """should raise when unable to read the data for the plateau"""
        with self.assertRaises(ValueError):
            process_lines.main([])
