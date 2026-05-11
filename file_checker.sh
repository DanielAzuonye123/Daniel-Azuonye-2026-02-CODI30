#!/bin/bash

# file_checker.sh
# Checks if a file exists

read -p "Enter a filename: " file

if [ -f "$file" ]
then
    echo "The file exists."
else
    echo "The file does not exist."
fi
