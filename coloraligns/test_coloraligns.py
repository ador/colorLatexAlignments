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
        self.inputAlignPathDna = "testdata/sample_align_DNA.fsa"
        self.colorDefsPath = "testdata/sample_colordef.txt"
        self.colorDefsPathDna = "testdata/sample_colordef_dna.txt"
        self.colorAligns = ColorLatexAligns()

    def test_read_inputs(self):
        seqs = self.colorAligns.read_fasta_input(self.inputAlignPath1)
        self.assertEqual(seqs[0].name, "alma")
        colorMap = self.colorAligns.read_color_map(self.colorDefsPath)
        self.assertEqual(colorMap['A'], ['148','194','53'])
        self.assertEqual(colorMap['Z'], ['245','250','119'])
        self.assertEqual(colorMap['Del'], ['255','255','255'])

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

    def test_create_latex_nocolor1(self):
        self.colorAligns.read_fasta_input(self.inputAlignPath1)
        latex_lines = self.colorAligns.create_latex_code(25, 8, True)
        self.assertEqual(len(latex_lines), 5)
        self.assertEqual("alma    E-WQFYIGGVF-", latex_lines[1])
        self.assertEqual("korte   -DWQ-YKSGV--", latex_lines[2])
        self.assertEqual("szilva  -D-QFYK-GIFE", latex_lines[3])

    def test_create_latex_nocolor2(self):
        self.colorAligns.read_fasta_input(self.inputAlignPath1)
        latex_lines = self.colorAligns.create_latex_code(6, 8, True)
        self.assertEqual(len(latex_lines), 10)
        self.assertEqual("alma    E-WQFY", latex_lines[1])
        self.assertEqual("korte   -DWQ-Y", latex_lines[2])
        self.assertEqual("szilva  -D-QFY", latex_lines[3])
        self.assertEqual("alma    IGGVF-", latex_lines[6])
        self.assertEqual("korte   KSGV--", latex_lines[7])
        self.assertEqual("szilva  K-GIFE", latex_lines[8])

    def test_transform_color_row(self):
        colorMap = self.colorAligns.read_color_map(self.colorDefsPath)
        self.assertEqual(colorMap['A'], ['148','194','53'])
        self.assertEqual(colorMap['Del'], ['255','255','255'])
        colordefA = self.colorAligns.get_latex_colordef('A')
        colordefZ = self.colorAligns.get_latex_colordef('Z')
        colordefDash = self.colorAligns.get_latex_colordef('-')
        self.assertEqual(colordefA, '\definecolor{colorA}{RGB}{148,194,53}')
        self.assertEqual(colordefZ, '\definecolor{colorZ}{RGB}{245,250,119}')
        self.assertEqual(colordefDash, '\definecolor{colorDel}{RGB}{255,255,255}')

    def test_latex_preamble(self):
        colorMap = self.colorAligns.read_color_map(self.colorDefsPath)
        preamble_rows = self.colorAligns.get_latex_preamble()
        self.assertEqual(r'\documentclass{article}', preamble_rows[0])
        self.assertEqual(r'\usepackage[utf8]{inputenc}', preamble_rows[1])
        self.assertEqual(r'\usepackage[english]{babel}', preamble_rows[2])
        self.assertEqual(r'\usepackage{fancyvrb}', preamble_rows[3])
        self.assertEqual(r'\usepackage[usenames, dvipsnames]{color}', preamble_rows[4])
        self.assertEqual(r'\usepackage{color}', preamble_rows[5])
        self.assertEqual(r'\usepackage{setspace}', preamble_rows[6])
        self.assertEqual(r'\usepackage{adjustbox}', preamble_rows[7])
        self.assertEqual(r'\definecolor{colorA}{RGB}{148,194,53}', preamble_rows[8])
        self.assertEqual(r'\definecolor{colorB}{RGB}{128,161,210}', preamble_rows[9])
        self.assertEqual(r'\definecolor{colorZ}{RGB}{245,250,119}', preamble_rows[34])

    def test_latex_pre_verbatim(self):
        colorMap = self.colorAligns.read_color_map(self.colorDefsPath)
        pre_rows = self.colorAligns.get_latex_pre_verbatim()
        self.assertEqual(28, len(pre_rows))
        self.assertEqual(r'\newcommand{\cA}[1]{\begingroup\fboxsep=1.5pt\colorbox{colorA}{#1}\endgroup}', pre_rows[0])
        self.assertEqual(r'\newcommand{\cB}[1]{\begingroup\fboxsep=1.5pt\colorbox{colorB}{#1}\endgroup}', pre_rows[1])
        self.assertEqual(r'\newcommand{\cDel}[1]{\begingroup\fboxsep=1.5pt\colorbox{colorDel}{#1}\endgroup}', pre_rows[3])
        self.assertEqual(r'\newcommand{\cZ}[1]{\begingroup\fboxsep=1.5pt\colorbox{colorZ}{#1}\endgroup}', pre_rows[26])
        self.assertEqual(r'\begin{Verbatim}[frame=single,baselinestretch=0.48,commandchars=\\\{\},codes={\catcode`$=3\catcode`^=7\catcode`_=8}]', pre_rows[27])

    def test_latex_post_verbatim(self):
        post_rows = self.colorAligns.get_latex_post_verbatim()
        self.assertEqual(r'\end{Verbatim}', post_rows[0])

    def test_create_latex_color1(self):
        self.colorAligns.read_fasta_input(self.inputAlignPath1)
        self.colorAligns.read_color_map(self.colorDefsPath)
        latex_lines = self.colorAligns.create_latex_code(6, 8, False)
        self.assertEqual(len(latex_lines), 10)
        self.assertEqual("alma    \cE{E}\cDel{-}\cW{W}\cQ{Q}\cF{F}\cY{Y}", latex_lines[1])
        self.assertEqual("korte   \cDel{-}\cD{D}\cW{W}\cQ{Q}\cDel{-}\cY{Y}", latex_lines[2])

    def test_create_latex_color2(self):
        self.colorAligns.read_fasta_input(self.inputAlignPathDna)
        self.colorAligns.read_color_map(self.colorDefsPathDna)
        latex_lines_dna = self.colorAligns.create_latex_code(6, 8, False, False, "dna")
        self.assertEqual(len(latex_lines_dna), 10)
        self.assertEqual(r'alma    \cCd{C}\cDel{-}\cTd{T}\cTd{T}\cAd{A}\cGd{G}' , latex_lines_dna[1])
        latex_lines_prot = self.colorAligns.create_latex_code(6, 8, False, False, "protein")
        self.assertEqual(len(latex_lines_prot), 10)
        self.assertEqual(r'alma    \cC{C}\cDel{-}\cT{T}\cT{T}\cA{A}\cG{G}' , latex_lines_prot[1])

    def test_marks_row_nomarks(self):
        self.colorAligns.read_fasta_input(self.inputAlignPath1)
        self.colorAligns.read_color_map(self.colorDefsPath)
        latex_lines = self.colorAligns.create_latex_code(6, 8, False, False)
        self.assertEqual(len(latex_lines), 10)
        self.assertEqual("", latex_lines[0])
        self.assertEqual("", latex_lines[5])

if __name__ == '__main__':
    unittest.main()
