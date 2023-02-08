#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

if [ "$PWD" != "$SCRIPT_DIR" ]; then
    cd "$SCRIPT_DIR" || exit
fi

if [ "$*" == "compile" ]; then
    (cd lib && make)
    make
elif [ "$*" == "run" ]; then
    (cd lib && make)
    make
    target/aoc-2022
elif [ "$*" == "clean" ]; then
    make clean
    (cd lib && make clean)
fi
