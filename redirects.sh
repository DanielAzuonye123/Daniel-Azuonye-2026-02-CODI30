#!/bin/bash

# =========================
# REDIRECTS (> and >>)
# =========================
# > overwrites a file
# >> appends to a file

# Overwrite file
echo "Hello file" > output.txt

# Append to file
echo "Another line" >> output.txt

# View file
cat output.txt

# Common mistake: using > instead of >> and losing data
