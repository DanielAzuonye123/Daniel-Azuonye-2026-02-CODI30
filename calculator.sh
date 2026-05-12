#!/bin/bash

# calculator.sh
# Simple calculator using Bash

read -p "Enter first number: " num1
read -p "Enter second number: " num2

echo
echo "Choose an operation:"
echo "1. Add"
echo "2. Subtract"
echo "3. Multiply"
echo "4. Divide"

read -p "Option: " option

case $option in
    1)
        echo "Result: $((num1 + num2))"
        ;;
    2)
        echo "Result: $((num1 - num2))"
        ;;
    3)
        echo "Result: $((num1 * num2))"
        ;;
    4)
        echo "Result: $((num1 / num2))"
        ;;
    *)
        echo "Invalid option."
        ;;
esac
