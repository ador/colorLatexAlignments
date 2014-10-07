class ColorLatexAligns(object):
    """A class that reads an input multiple
    sequence alignment (fasta format) and
    prints out a latex code chunk that
    colors the alignment"""

    colormap = dict()

    def readInput(self, path):
        f = open(path, 'r')
        return f.readlines()

    def readColorMap(self, path):
        f = open(path, 'r')
        for line in f.readlines():
            (letter, rgbtext) = line.split(' ')
            rgb = rgbtext.strip().lstrip('{').rstrip('}').split(',')
            self.colormap[letter] = rgb
        return self.colormap

