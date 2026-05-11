#!/bin/bash

# loops.sh
# Demonstrates basic Bash loops

echo "===== FOR LOOP EXAMPLE ====="

for number in 1 2 3 4 5
do
    echo "Current number: $number"
done

echo
echo "===== LOOPING THROUGH NAMES ====="

for name in Daniel Alex Sarah Mike
do
    echo "Hello, $name"
done

echo
echo "===== COUNTING LOOP ====="

for (( i=1; i<=5; i++ ))
do
    echo "Count: $i"
done
