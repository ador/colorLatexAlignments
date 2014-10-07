import unittest
from coloraligns import ColorLatexAligns

class TestColorLatexAligns(unittest.TestCase):

    def setUp(self):
        self.indata = "test"

    def test_read_input(self):
        self.assertEqual(self.indata, "test")

        # should raise an exception for an unreadable file
        # TODO self.assertRaises(IOError, )

if __name__ == '__main__':
    unittest.main()