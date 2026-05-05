#!/bin/bash

# IF / ELSE IN BASH
# used to make decisions

num=10

if [ $num -gt 5 ]
then
    echo "Number is bigger than 5"
else
    echo "Number is 5 or smaller"
fi

# elif = extra condition

num=5

if [ $num -gt 5 ]
then
    echo "Big number"
elif [ $num -eq 5 ]
then
    echo "Number is exactly 5"
else
    echo "Small number"
fi

# quick idea:
# if = first check
# elif = second check
# else = fallback
