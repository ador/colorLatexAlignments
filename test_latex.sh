#!/bin/bash -eu

baseDir="$(dirname "$0")"

pushd "$baseDir" > /dev/null

  python3 coloraligns/apply_colors.py -i testdata/sample_align_short3.fsa -c sampledata/colordef.txt -l 20 -n 10 -o generated_sample_doc.tex
  pdflatex generated_sample_doc.tex

  python3 coloraligns/apply_colors.py -i testdata/sample_abc_align.fsa -c sampledata/colordef.txt -l 20 -n 10 -s Large -o generated_abc_doc.tex
  pdflatex generated_abc_doc.tex

popd > /dev/null





