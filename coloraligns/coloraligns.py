from fastareader import FastaReader

class ColorLatexAligns(object):
    """A class that reads an input multiple
    sequence alignment (fasta format) and
    prints out a latex code chunk that
    colors the alignment"""

    colormap = dict()
    reader = FastaReader()
    outlines = list()
    sequences = []


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

        for seq in self.sequences:
            self.outlines.append(seq.get_seq() + "\n")
        return self.outlines


    def write_output(self):
        pass
