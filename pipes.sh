#!/bin/bash

# =========================
# PIPES ( | )
# =========================
# Pipes send output of one command into another.

# Example: list files and filter with grep
ls | grep ".sh"

# Example: count files
ls | wc -l

# Example: sort text
echo -e "banana\napple\ncarrot" | sort
