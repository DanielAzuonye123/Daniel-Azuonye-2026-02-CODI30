#!/bin/bash

# CONDITIONALS IN BASH
# used to compare values and make decisions

a=10
b=5

# EQUAL TO

if [ $a -eq $b ]
then
    echo "a is equal to b"
else
    echo "a is NOT equal to b"
fi

# GREATER / LESS

if [ $a -gt $b ]
then
    echo "a is greater than b"
fi

if [ $a -lt $b ]
then
    echo "a is less than b"
fi

# quick meaning:
# -eq = equal
# -gt = greater than
# -lt = less than
