#!/bin/bash

#! Sprawdzenie czy argumenty są poprawne
if [[ $# -ne 1 ]]; then
  echo "err wrong arg number" >&2
  exit 1
elif [[ ! -f $1 ]]; then
  echo "err argument is not a file path" >&2
  exit 1
elif [[ $1 != *.jpg ]]; then
  echo "err file is not JPG image" >&2
  exit 1
fi

#! execution of exiftool with GPS data
image=$1
exiftool -gps* $image
