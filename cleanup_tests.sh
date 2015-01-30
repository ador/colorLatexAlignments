#!/bin/bash

baseDir="$(dirname "$0")"

pushd "$baseDir" > /dev/null

  rm generated_abc_doc.tex 2>/dev/null
  rm generated_abc_doc.log 2>/dev/null
  rm generated_abc_doc.aux 2>/dev/null
  rm generated_sample_doc.tex 2>/dev/null
  rm generated_sample_doc.log 2>/dev/null
  rm generated_sample_doc.aux 2>/dev/null

popd > /dev/null
