import unittest
from coloraligns import ColorLatexAligns

class TestColorLatexAligns(unittest.TestCase):

    def setUp(self):
        self.inputAlignPath1 = "testdata/sample_align_short3.fsa"
        self.colorDefsPath = "testdata/sample_colordef.txt"
        self.colorAligns = ColorLatexAligns()

    def test_read_inputs(self):
        seqs = self.colorAligns.read_fasta_input(self.inputAlignPath1)
        self.assertEqual(seqs[0].get_name(), "alma")
        colorMap = self.colorAligns.read_color_map(self.colorDefsPath)
        self.assertEqual(colorMap['A'], ['148','194','53'])
        self.assertEqual(colorMap['Z'], ['245','250','119'])

    def test_read_bad_colorfile(self):
        self.assertRaises(FileNotFoundError, self.colorAligns.read_color_map, "notexisting.txt")

    def test_create_latex(self):
        self.colorAligns.read_fasta_input(self.inputAlignPath1)
        self.colorAligns.read_color_map(self.colorDefsPath)
        latex_lines = self.colorAligns.create_latex_code(10)
        self.assertEqual(len(latex_lines), 3)
        self.assertEqual("E-WQFYIGGVF-\n", latex_lines[0])

if __name__ == '__main__':
    unittest.main()