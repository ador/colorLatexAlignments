#!/bin/bash

pushd `dirname $0` > /dev/null
baseDir=`pwd -P`

python3 coloraligns/apply_colors.py -i testdata/sample_align_short3.fsa -c testdata/sample_colordef.txt -l 20 -o sample.tex

# TODO
#pdflatex sample.tex

popd > /dev/null





