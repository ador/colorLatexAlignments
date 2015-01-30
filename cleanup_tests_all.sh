#!/bin/bash

baseDir="$(dirname "$0")"

pushd "$baseDir" > /dev/null

  ./cleanup_tests.sh
  rm generated_*.tex 2>/dev/null
  rm generated_*.pdf 2>/dev/null
  rm conus_sample1.tex 2>/dev/null
  rm conus_sample1.pdf 2>/dev/null
  rm conus_sample2.tex 2>/dev/null
  rm dna_sample.pdf 2>/dev/null
  rm dna_sample.tex 2>/dev/null
  rm conus_sample.pdf 2>/dev/null
  rm *.aux 2>/dev/null
  rm *.log 2>/dev/null

popd > /dev/null
