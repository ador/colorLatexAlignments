#!/bin/bash

baseDir="$(dirname "$0")"

pushd "$baseDir" > /dev/null

  ./cleanup_tests.sh
  rm generated_*.tex 2>/dev/null
  rm generated_*.pdf 2>/dev/null
  rm *.aux 2>/dev/null
  rm *.log 2>/dev/null

popd > /dev/null
