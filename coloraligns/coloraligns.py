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
        f = open(path, 'r')
        for line in f.readlines():
            (letter, rgbtext) = line.split(' ')
            rgb = rgbtext.strip().lstrip('{').rstrip('}').split(',')
            self.colormap[letter] = rgb
        f.close()
        return self.colormap


    def create_latex_code(self, width):

        for seqobj in self.sequences:
            self.outlines.append(seqobj.seq + "\n")
        return self.outlines


    def write_output(self):
        pass
