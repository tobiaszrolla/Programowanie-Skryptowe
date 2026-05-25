#!/bin/bash

#! check arguments
if [[ $# -ne 1 ]]; then
  echo "err wrong arg number" >&2
  exit 1
elif [[ ! -f $1 ]]; then
  echo "err arg is not a file path" >&2
  exit 1
elif [[ $1 != *.jpg ]]; then
  echo "err arg is not JPG file" >&2
  exit 1
fi

#Making clear image
image=$1
rm -f clean.jpg
exiftool -all= -o clean.jpg $image
