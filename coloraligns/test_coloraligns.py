import unittest
from coloraligns import ColorLatexAligns

class TestColorLatexAligns(unittest.TestCase):

    def setUp(self):
        self.inputAlignPath1 = "testdata/sample_align_short3.fsa"
        self.colorDefsPath = "testdata/sample_colordef.txt"
        self.colorAligns = ColorLatexAligns()

    def test_read_inputs(self):
        alignLines = self.colorAligns.readInput(self.inputAlignPath1)
        self.assertEqual(alignLines[0].strip(), ">alma")
        colorMap = self.colorAligns.readColorMap(self.colorDefsPath)
        self.assertEqual(colorMap['A'], ['148','194','53'])
        self.assertEqual(colorMap['Z'], ['245','250','119'])
        # should raise an exception for an unreadable file
        # TODO self.assertRaises(IOError, )

if __name__ == '__main__':
    unittest.main()