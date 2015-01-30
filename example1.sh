#!/bin/bash -eu

# just making sure that this script can be run from anywhere (not just from its own directory)
baseDir=$(dirname "$0")
thisAbsDir=$(readlink -f "$baseDir")
export PYTHONPATH="$thisAbsDir:${PYTHONPATH:-}"

pushd "$baseDir" > /dev/null

  # this is how you call the python script
  # -i <file> : input alignment (currently only fasta format is supported)
  # -c <file> : color-definitions
  # -l <int>  : maximum number of sequence-characters(plus gaps) in an alignment line
  # -n <int>  : maximum number of characters for sequence names (names will be truncated if too long)
  # -o <file> : output tex file name (this will be a proper latex document, fragments can be copied into a real document)
  python3 coloraligns/apply_colors.py -i sampledata/conus-example-aligned.fasta -c testdata/sample_colordef.txt -l 32 -n 14 -o conus_sample.tex

  pdflatex conus_sample.tex

popd > /dev/null
