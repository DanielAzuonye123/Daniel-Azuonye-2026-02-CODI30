#!/bin/bash

# case_menu.sh
# Demonstrates a basic case/esac menu

echo "===== MAIN MENU ====="
echo "1. Say Hello"
echo "2. Show Date"
echo "3. Show Current User"
echo "4. Exit"

echo
read -p "Choose an option (1-4): " option

case $option in
    1)
        echo "Hello, welcome to Bash scripting!"
        ;;
    2)
        date
        ;;
    3)
        whoami
        ;;
    4)
        echo "Exiting program..."
        ;;
    *)
        echo "Invalid option."
        ;;
esac
