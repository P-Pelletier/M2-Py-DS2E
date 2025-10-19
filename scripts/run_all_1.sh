#!/bin/bash

for f in 1_*.py; do
    echo "--- Running $f ---"
    python3 "$f"
    echo
    echo "=============================="
done
