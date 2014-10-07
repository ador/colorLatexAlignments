#!/bin/bash

pushd `dirname $0` > /dev/null
baseDir=`pwd -P`
popd > /dev/null


python3 ${baseDir}/coloraligns/test_sequence.py
python3 ${baseDir}/coloraligns/test_fastareader.py
python3 ${baseDir}/coloraligns/test_coloraligns.py

${baseDir}/test_latex.sh
