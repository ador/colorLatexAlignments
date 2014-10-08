import math
from fastareader import FastaReader

class ColorLatexAligns(object):
    """A class that reads an input multiple
    sequence alignment (fasta format) and
    prints out a latex code chunk that
    colors the alignment"""

    def __init__(self):
        self.colormap = dict()
        self.reader = FastaReader()
        self.outlines = list()
        self.sequences = []

    def read_fasta_input(self, path):
        self.sequences = self.reader.read_seqs(path)
        return self.sequences


    def read_color_map(self, path):
        with open(path, 'r') as f:
            for line in f.readlines():
                (letter, rgbtext) = line.split(' ')
                rgb = rgbtext.strip().lstrip('{').rstrip('}').split(',')
                self.colormap[letter] = rgb
            f.close()
        return self.colormap

    def fixwidth(self, name, width):
        if len(name) > width:
            return name[0:width]
        else:
            return name.ljust(width)

    def outrow_indexer(self, ith_seq, nth_row_in_seq):
        seq_num = len(self.sequences)
        return ith_seq + nth_row_in_seq * (seq_num + 2) + 1

    def howmany_rows_per_seq(self, seqwidth):
        # assuming all seq lengths are equal because it's an alignment
        seq_len = len(self.sequences[0].seq)
        num_rows = math.ceil(1.0 * seq_len / seqwidth)
        return num_rows

    def howmany_rows_total(self, seqwidth):
        seq_num = len(self.sequences)
        rows_per_seq = self.howmany_rows_per_seq(seqwidth)
        return (seq_num + 2) * (rows_per_seq)

    def create_latex_code(self, seqwidth, namewidth, nocolor=False):
        if len(self.sequences) < 1:
            return list()
        # precomputing row number because we have to interleave results
        num_rows_to_return = self.howmany_rows_total(seqwidth)
        self.outlines = [None] * num_rows_to_return

        for seqobj in self.sequences:
            if nocolor:
                self.outlines.append(self.fixwidth(seqobj.name, namewidth)
                                     + seqobj.seq + "\n")
            else:
                self.outlines.append()
        return self.outlines


    def write_output(self, outpath):
        pass
