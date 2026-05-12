#!/bin/bash

# two_dimensional_arrays.sh
# Bash does not support true two-dimensional arrays.
# However, we can logically associate multiple arrays together
# using matching indexes.

echo "===== LOGICALLY ASSOCIATED ARRAYS ====="

# First array stores student names
students=("Daniel" "Alex" "Sarah" "Mike")

# Second array stores grades
grades=(95 88 91 76)

echo
echo "Student Grades:"
echo "----------------"

# Loop through arrays using indexes
for i in "${!students[@]}"
do
    echo "${students[$i]} scored ${grades[$i]}%"
done

echo
echo "===== EXPLANATION ====="

echo "Bash does not have true two-dimensional arrays."
echo "Instead, we use multiple arrays and connect them using indexes."
echo "For example:"
echo "students[0] matches grades[0]"
echo "students[1] matches grades[1]"

echo
echo "===== WHY TWO-DIMENSIONAL ARRAYS ARE USEFUL ====="

echo "In languages like Python, two-dimensional arrays can store"
echo "data in rows and columns like a table or spreadsheet."

echo
echo "Examples of use cases:"
echo "- Student grade tables"
echo "- Game boards"
echo "- Spreadsheets"
echo "- Seating charts"
echo "- Inventory systems"

