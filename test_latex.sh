#!/bin/bash -eu

baseDir="$(dirname "$0")"

pushd "$baseDir" > /dev/null

  python3 coloraligns/apply_colors.py -i testdata/sample_align_short3.fsa -c testdata/sample_colordef.txt -l 20 -o sample.tex

  cat testdata/document_firstpart.tex sample.tex > generated_align_document.tex
  # TODO
  # pdflatex generated_align_document.tex

popd > /dev/null





