import math
from fastareader import FastaReader
from string import ascii_uppercase

class ColorLatexAligns(object):
    """A class that reads an input multiple
    sequence alignment (fasta format) and
    prints out a latex code chunk that
    colors the alignment.
    """

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

    def get_latex_colordef(self, char):
        if self.colormap[char] != None:
            (R, G, B) = self.colormap[char]
            cdef = "\definecolor{{color{letter}}}{{RGB}}{{{r},{g},{b}}}".format(letter=char, r=R, g=G, b=B)
            return cdef

    def get_latex_colordefs_capitals(self):
        ret = list()
        for letter in ascii_uppercase:
            latex_part = self.get_latex_colordef(letter)
            ret.append(latex_part)
        return ret

    def get_latex_preamble(self):
        ret = list()
        ret.append(r'\usepackage{fancyvrb}')
        ret.append(r'\usepackage[usenames, dvipsnames]{color}')
        ret.append(r'\usepackage{color}')
        ret.append(r'\usepackage{setspace}')
        ret.extend(self.get_latex_colordefs_capitals())
        return ret

    def get_latex_pre_verbatim(self):
        ret = list()
        for letter in ascii_uppercase:
            color_newcommand = r'\newcommand{\c' + letter + r'}[1]{\begingroup\fboxsep=1.5pt\colorbox{color' + letter + r'}{#1}\endgroup}'
            ret.append(color_newcommand)
        ret.append(r'\begin{Verbatim}[frame=single,baselinestretch=0.48,commandchars=\\\{\},codes={\catcode`$=3\catcode`^=7\catcode`_=8}]')
        return ret

    def get_latex_post_verbatim(self):
        ret = list()
        ret.append(r'\end{Verbatim}')
        return ret

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

    def color_letters(self, seq_part):
        ret = ""
        for letter in seq_part:
            if letter == '-':
                ret = ret + '-'
            else:
                one_colored_letter = r'\c' + letter + r'{' + letter + r'}'
                ret = ret + one_colored_letter
        return ret

    def create_latex_code(self, seq_width, name_width, nocolor=False):
        if len(self.sequences) < 1:
            return list()
        # precomputing row number because we have to interleave results
        rows_per_seq = self.howmany_rows_per_seq(seq_width)
        num_rows_to_return = self.howmany_rows_total(seq_width)
        self.outlines = [None] * num_rows_to_return
        num_of_seqs = len(self.sequences)

        for i in range(rows_per_seq):
            self.outlines[(i * (num_of_seqs + 2))] = "   todo * *:. *"
            self.outlines[(i * (num_of_seqs + 2) + num_of_seqs + 1)] = "- - - - - -"

        for seq_idx, seq_obj in enumerate(self.sequences):
            seq_rows = seq_obj.wrap_seq(seq_width)
            for row_idx, seq_row in enumerate(seq_rows):
                out_idx = self.outrow_indexer(seq_idx, row_idx)
                if nocolor:
                    self.outlines[out_idx] = self.fixwidth(seq_obj.name, name_width) + seq_rows[row_idx]
                else:
                    self.outlines[out_idx] = self.fixwidth(seq_obj.name, name_width) + self.color_letters(seq_rows[row_idx])
        return self.outlines


    def write_output(self, outpath):
        pass
