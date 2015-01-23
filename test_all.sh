#!/bin/bash -eu

baseDir=$(dirname "$0")
thisAbsDir=$(readlink -f "$baseDir")
export PYTHONPATH="$thisAbsDir:${PYTHONPATH:-}"

pushd "$baseDir" > /dev/null

  python3 coloraligns/test_sequence.py
  python3 coloraligns/test_fastareader.py
  python3 coloraligns/test_coloraligns.py

  ./test_latex.sh

popd > /dev/null
