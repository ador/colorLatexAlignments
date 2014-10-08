#!/bin/bash -eu

baseDir=$(dirname "$0")
thisAbsDir=$(readlink -f "$baseDir")
export PYTHONPATH="$thisAbsDir:${PYTHONPATH:-}"

python3 "$baseDir"/coloraligns/test_sequence.py
python3 "$baseDir"/coloraligns/test_fastareader.py
python3 "$baseDir"/coloraligns/test_coloraligns.py

#${baseDir}/test_latex.sh
