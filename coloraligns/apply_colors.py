import argparse
from coloraligns import ColorLatexAligns


parser = argparse.ArgumentParser()
parser.add_argument('-i', help='input file in fasta format')
parser.add_argument('-o', help='output tex file')
parser.add_argument('-c', help='color definition file')
parser.add_argument('-l', help='maximum line width in characters')
args = parser.parse_args()

# TODO

colorAligns = ColorLatexAligns()
colorAligns.read_fasta_input(args.i)
colorAligns.read_color_map(args.c)
