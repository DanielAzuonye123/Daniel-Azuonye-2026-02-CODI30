#!/bin/bash

# while_loops.sh
# Demonstrates basic while loops in Bash

counter=1

echo "===== BASIC WHILE LOOP ====="

while [ $counter -le 5 ]
do
    echo "Counter: $counter"
    ((counter++))
done

echo
echo "Loop finished."

echo
echo "===== USER INPUT LOOP ====="

answer=""

while [ "$answer" != "yes" ]
do
    read -p "Type 'yes' to continue: " answer
done

echo "Thank you!"
