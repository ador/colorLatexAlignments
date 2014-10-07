class ColorLatexAligns(object):
    """A class that reads an input multiple
    sequence alignment (fasta format) and
    prints out a latex code chunk that
    colors the alignment"""

    colormap = dict()

    def read_fasta_input(self, path):
        f = open(path, 'r')
        lines = f.readlines()
        f.close()
        return lines

    def read_color_map(self, path):
        f = open(path, 'r')
        for line in f.readlines():
            (letter, rgbtext) = line.split(' ')
            rgb = rgbtext.strip().lstrip('{').rstrip('}').split(',')
            self.colormap[letter] = rgb
        f.close()
        return self.colormap

