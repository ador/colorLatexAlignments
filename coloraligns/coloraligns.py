from fastareader import FastaReader

class ColorLatexAligns(object):
    """A class that reads an input multiple
    sequence alignment (fasta format) and
    prints out a latex code chunk that
    colors the alignment"""

    colormap = dict()
    reader = FastaReader()


    def read_fasta_input(self, path):
        sequences = self.reader.read_seqs(path)
        return sequences

    def read_color_map(self, path):
        f = open(path, 'r')
        for line in f.readlines():
            (letter, rgbtext) = line.split(' ')
            rgb = rgbtext.strip().lstrip('{').rstrip('}').split(',')
            self.colormap[letter] = rgb
        f.close()
        return self.colormap

