#!/bin/bash

# =========================
# CASE STATEMENTS
# =========================
# Used instead of multiple if/else conditions.

read -p "Enter a fruit: " fruit

case $fruit in
    apple)
        echo "You chose apple"
        ;;
    banana)
        echo "You chose banana"
        ;;
    *)
        echo "Unknown fruit"
        ;;
esac
