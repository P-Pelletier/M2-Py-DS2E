#!/bin/bash

for f in 2_*.py; do
    echo "--- Running $f ---"
    python3 "$f"
    echo
    echo "=============================="
done
