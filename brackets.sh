#!/bin/bash

# BRACKETS IN BASH
# We use brackets to check if something is true or false

num=10

# single brackets [ ]
# basic way to check conditions

if [ $num -gt 5 ]
then
    echo "Number is bigger than 5"
fi

# double brackets [[ ]]
# same idea, just safer and better

if [[ $num -gt 5 ]]
then
    echo "Still bigger than 5"
fi

# quick meaning:
# -gt = greater than
# -lt = less than
# -eq = equal

# IMPORTANT:
# always leave spaces inside brackets
# [ $num -gt 5 ] NOT [$num-gt5]
