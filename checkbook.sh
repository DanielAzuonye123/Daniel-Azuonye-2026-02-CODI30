#!/bin/bash

# =========================
# SIMPLE CHECKBOOK APP
# =========================
# This script tracks a basic balance and allows:
# - viewing balance
# - depositing money
# - withdrawing money

BALANCE=0

show_balance() {
    echo "Current Balance: $BALANCE"
}

deposit() {
    read -p "Enter amount to deposit: " amount
    BALANCE=$((BALANCE + amount))
    echo "Deposited: $amount"
}

withdraw() {
    read -p "Enter amount to withdraw: " amount

    if [ $amount -gt $BALANCE ]; then
        echo "Not enough funds!"
    else
        BALANCE=$((BALANCE - amount))
        echo "Withdrawn: $amount"
    fi
}

# MENU
while true
do
    echo "===================="
    echo "1. Show Balance"
    echo "2. Deposit"
    echo "3. Withdraw"
    echo "4. Exit"
    echo "===================="

    read -p "Choose option: " choice

    case $choice in
        1) show_balance ;;
        2) deposit ;;
        3) withdraw ;;
        4) echo "Goodbye"; break ;;
        *) echo "Invalid option" ;;
    esac

done
