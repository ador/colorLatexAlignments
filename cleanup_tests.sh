#!/bin/bash

baseDir="$(dirname "$0")"

pushd "$baseDir" > /dev/null

  rm generated_abc_align_document.tex 2>/dev/null
  rm generated_align_document.tex 2>/dev/null
  rm generated_abc_sample.tex 2>/dev/null
  rm generated_align_document.log 2>/dev/null
  rm generated_align_document.aux 2>/dev/null
  rm generated_abc_align_document.log 2>/dev/null
  rm generated_abc_align_document.aux 2>/dev/null

popd > /dev/null
