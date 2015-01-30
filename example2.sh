#!/bin/bash -eu

baseDir=$(dirname "$0")
thisAbsDir=$(readlink -f "$baseDir")
export PYTHONPATH="$thisAbsDir:${PYTHONPATH:-}"

pushd "$baseDir" > /dev/null

  python3 coloraligns/apply_colors.py -i sampledata/conus-example-aligned.fasta -c sampledata/colordef.txt -l 38 -n 14 --small=True -o conus_sample.tex

  pdflatex conus_sample.tex

popd > /dev/null
