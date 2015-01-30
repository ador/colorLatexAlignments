#!/bin/bash -eu

baseDir=$(dirname "$0")
thisAbsDir=$(readlink -f "$baseDir")
export PYTHONPATH="$thisAbsDir:${PYTHONPATH:-}"

pushd "$baseDir" > /dev/null

  python3 coloraligns/apply_colors.py -i sampledata/small-dna-example.fasta -c sampledata/colordef_dna.txt -l 38 -n 10 -s Large -o dna_sample.tex

  pdflatex dna_sample.tex

popd > /dev/null