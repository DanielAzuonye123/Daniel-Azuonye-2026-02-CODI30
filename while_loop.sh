#!/bin/bash

# =========================
# WHILE LOOPS
# =========================
# A while loop runs while a condition is true.

counter=1

while [ $counter -le 5 ]
do
    echo "Counter is: $counter"
    counter=$((counter + 1))
done

# Common mistake: forgetting to update counter → infinite loop
