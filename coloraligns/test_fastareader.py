import unittest
from fastareader import FastaReader, DuplicateSeqNameException

class TestFastaReader(unittest.TestCase):

    def setUp(self):
        self.input_align_path_1 = "testdata/sample_align_short3.fsa"
        self.input_align_path_2 = "testdata/sample_align_short3_bad.fsa"
        self.input_align_path_3 = "testdata/sample_align_short6.fsa"
        self.reader = FastaReader()

    def test_read1(self):
        sequence_list = self.reader.read_seqs(self.input_align_path_1)
        self.assertEqual(len(sequence_list), 3)
        self.assertEqual(sequence_list[0].get_name(), "alma")

    def test_read_bad(self):
        self.assertRaises(DuplicateSeqNameException, self.reader.read_seqs, self.input_align_path_2)

    def test_read3(self):
        sequence_list = self.reader.read_seqs(self.input_align_path_3)
        self.assertEqual(len(sequence_list), 6)
        self.assertEqual(sequence_list[0].get_name(), "alma")
        self.assertEqual(sequence_list[1].get_name(), "korte")
        self.assertEqual(sequence_list[1].get_seq(), "-DWQ-YKSGV--")
        self.assertEqual(sequence_list[1].seq_without_gaps(), "DWQYKSGV")
        self.assertEqual(sequence_list[5].get_name(), "gimmme")



if __name__ == '__main__':
    unittest.main()