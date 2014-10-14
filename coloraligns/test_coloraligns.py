import unittest
from coloraligns import ColorLatexAligns

class TestColorLatexAligns(unittest.TestCase):

    def print_lines(self, lines):
        print("------start--------")
        for line in lines:
            print(line)
        print("------END--------")

    def setUp(self):
        self.inputAlignPath1 = "testdata/sample_align_short3.fsa"
        self.colorDefsPath = "testdata/sample_colordef.txt"
        self.colorAligns = ColorLatexAligns()

    def test_read_inputs(self):
        seqs = self.colorAligns.read_fasta_input(self.inputAlignPath1)
        self.assertEqual(seqs[0].name, "alma")
        colorMap = self.colorAligns.read_color_map(self.colorDefsPath)
        self.assertEqual(colorMap['A'], ['148','194','53'])
        self.assertEqual(colorMap['Z'], ['245','250','119'])

    def test_read_bad_colorfile(self):
        self.assertRaises(FileNotFoundError, self.colorAligns.read_color_map, "notexisting.txt")

    def test_numrows(self):
        self.colorAligns.read_fasta_input(self.inputAlignPath1)
        computed20 = self.colorAligns.howmany_rows_total(20)
        self.assertEqual(computed20, 5)
        computed8 = self.colorAligns.howmany_rows_total(8)
        self.assertEqual(computed8, 10)
        computed4 = self.colorAligns.howmany_rows_total(4)
        self.assertEqual(computed4, 15)

    def test_indexer1(self):
        self.colorAligns.read_fasta_input(self.inputAlignPath1)
        latex_lines = self.colorAligns.create_latex_code(20, 8, True)
        self.assertEqual(len(latex_lines), 5)
        #self.print_lines(latex_lines)

    def test_indexer2(self):
        self.colorAligns.read_fasta_input(self.inputAlignPath1)
        latex_lines = self.colorAligns.create_latex_code(8, 8, True)
        self.assertEqual(len(latex_lines), 10)
        #self.print_lines(latex_lines)

    def test_create_latex1(self):
        self.colorAligns.read_fasta_input(self.inputAlignPath1)
        self.colorAligns.read_color_map(self.colorDefsPath)
        latex_lines = self.colorAligns.create_latex_code(25, 8, True)
        self.assertEqual(len(latex_lines), 5)
        self.assertEqual("alma    E-WQFYIGGVF-", latex_lines[1])
        self.assertEqual("korte   -DWQ-YKSGV--", latex_lines[2])
        self.assertEqual("szilva  -D-QFYK-GIFE", latex_lines[3])


if __name__ == '__main__':
    unittest.main()