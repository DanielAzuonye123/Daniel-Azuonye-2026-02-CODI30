#!/bin/bash

# =========================
# SIMPLE TASK CHECKBOOK
# =========================
# This script helps track tasks and mark them as DONE or NOT DONE

tasks=("Functions" "While Loops" "For Loops" "Pipes" "Redirects" "Case Statements")

show_tasks() {
    echo "===================="
    echo "YOUR TASK CHECKLIST"
    echo "===================="

    for i in "${!tasks[@]}"
    do
        echo "$((i+1)). ${tasks[$i]} - NOT DONE"
    done

    echo "===================="
}

mark_done() {
    read -p "Enter task number to mark DONE: " num

    if [ $num -ge 1 ] && [ $num -le ${#tasks[@]} ]; then
        echo "✔ ${tasks[$((num-1))]} marked as DONE"
    else
        echo "Invalid task number"
    fi
}

while true
do
    echo ""
    echo "1. Show Tasks"
    echo "2. Mark Task as Done"
    echo "3. Exit"

    read -p "Choose option: " choice

    case $choice in
        1) show_tasks ;;
        2) mark_done ;;
        3) echo "Goodbye"; break ;;
        *) echo "Invalid option" ;;
    esac
done
