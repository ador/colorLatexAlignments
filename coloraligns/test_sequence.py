import unittest
from sequence import Sequence

class TestSequence(unittest.TestCase):

    def test_new_sequence(self):
        seq1 = Sequence("seqName", ["AAAACCC"])
        seq2 = Sequence("seqName2", ["AAAACCC", "CCEEEAA", "LLVAS"])

    def test_get_name(self):
        seq1 = Sequence("seqName", ["AAAACCC"])
        self.assertEqual(seq1.name, "seqName")

    def test_get_seq1(self):
        seq1 = Sequence("seqName", ["AAAACCC"])
        self.assertEqual(seq1.seq, "AAAACCC")

    def test_get_seq2(self):
        seq2 = Sequence("seqName2", ["AAAACCC", "DDEEEAA", "LLVAS"])
        self.assertEqual(seq2.seq, "AAAACCCDDEEEAALLVAS")

    def test_wrap(self):
        seq2 = Sequence("seqName2", ["AAAACCC", "DDEEEAA", "LLVAS"])
        self.assertEqual(seq2.wrap_seq(8), ["AAAACCCD", "DEEEAALL", "VAS"])
        self.assertEqual(seq2.wrap_seq(5), ["AAAAC", "CCDDE", "EEAAL", "LVAS"])
        self.assertEqual(seq2.wrap_seq(10), ["AAAACCCDDE", "EEAALLVAS"])

if __name__ == '__main__':
    unittest.main()