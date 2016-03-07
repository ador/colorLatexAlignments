ColorLatexAlignments
====================

A simple tool to generate LaTeX code from an input multiple alignment (fasta file format).
A color scheme can be specified, in which each amino acid (or DNA/RNA base) has its own color.


How to install
--------------

There is not much to install. But you will need some general tools: `pdflatex` and `python3`.

On Ubuntu, it means you should have these packages installed:<br />
`python3 texlive-latex-base texlive-latex-extra`

Run the tests in the top level directory within the git repository to check if everything is working:<br />
`$ ./test_all.sh`


How to use
----------
Have a look at the example scripts: `example1.sh`, `example2.sh` and 
`example3.sh`.

Or print the help menu:<br />
`$ python3 coloraligns/apply_colors.py --help`




