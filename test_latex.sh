#!/bin/bash -eu

baseDir="$(dirname "$0")"

pushd "$baseDir" > /dev/null

  python3 coloraligns/apply_colors.py -i testdata/sample_align_short3.fsa -c testdata/sample_colordef.txt -l 20 -n 10 -o generated_sample.tex
  cat testdata/document_firstpart.tex generated_sample.tex testdata/document_ending.tex > generated_align_document.tex
  pdflatex generated_align_document.tex

  python3 coloraligns/apply_colors.py -i testdata/sample_abc_align.fsa -c testdata/sample_colordef.txt -l 20 -n 10 -o generated_abc_sample.tex
  cat testdata/document_firstpart.tex generated_abc_sample.tex testdata/document_ending.tex > generated_abc_align_document.tex
  pdflatex generated_abc_align_document.tex

popd > /dev/null





