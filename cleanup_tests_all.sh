#!/bin/bash

baseDir="$(dirname "$0")"

pushd "$baseDir" > /dev/null

  ./cleanup.sh
  rm generated_sample.tex 2>/dev/null
  rm generated_align_document.pdf 2>/dev/null
  rm generated_abc_align_document.pdf 2>/dev/null

popd > /dev/null
