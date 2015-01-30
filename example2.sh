#!/bin/bash -eu

baseDir=$(dirname "$0")
thisAbsDir=$(readlink -f "$baseDir")
export PYTHONPATH="$thisAbsDir:${PYTHONPATH:-}"

pushd "$baseDir" > /dev/null

  python3 coloraligns/apply_colors.py -i sampledata/conus-example-aligned.fasta -c sampledata/colordef.txt -l 38 -n 14 -s footnotesize -o conus_sample2.tex

  pdflatex conus_sample2.tex

popd > /dev/null
