import argparse
from coloraligns import ColorLatexAligns


parser = argparse.ArgumentParser()
parser.add_argument('-i', help='input file in fasta format')
parser.add_argument('-o', help='output tex file')
parser.add_argument('-c', help='color definition file')
parser.add_argument('-l', help='maximum width (number of characters within a line - with gaps included) of the aligned sequence part')
parser.add_argument('-n', help='maximum number of characters for sequence names (names will be truncated if too long)')
parser.add_argument('-t', help='alignment type: "protein" (default) or "dna"')
parser.add_argument('-s', dest='size', default="normalsize", help='use different character sizes (valid values in decreasing size: "large", "normalsize" (default), "small", "footnotesize")')

args = parser.parse_args()


colorAligns = ColorLatexAligns()
colorAligns.read_fasta_input(args.i)
colorAligns.read_color_map(args.c)
if args.t == None:
    colorAligns.create_latex_code(int(args.l), int(args.n), False, False)
else:
    colorAligns.create_latex_code(int(args.l), int(args.n), False, False, args.t)
colorAligns.write_output(args.o, args.size)



