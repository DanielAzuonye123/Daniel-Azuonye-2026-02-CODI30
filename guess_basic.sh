#!/bin/bash
# This script is a basic number guessing game
# The user has to guess a number between 1 and 100

# Generate a random number between 1 and 100
# RANDOM generates a number between 0–32767
# % 100 makes it between 0–99
# +1 shifts range to 1–100
number=$((RANDOM % 100 + 1))

# Start a loop that continues until the user guesses correctly
while true; do

  # Prompt the user for a guess
  # Store the input in variable "guess"
  read -p "Guess a number between 1 and 100: " guess

  # Check if guess is less than the target number
  if [[ $guess -lt $number ]]; then
    echo "Too low"  # Tell user guess is too low

  # Check if guess is greater than the target number
  elif [[ $guess -gt $number ]]; then
    echo "Too high"  # Tell user guess is too high

  # If guess is neither too low nor too high, it must be correct
  else
    echo "Correct!"  # Congratulate user
    break            # Exit the loop
  fi

done

#!/bin/bash
# This script takes 10 numbers from the user and sorts them
# The user can choose sort options: -r (reverse), -u (unique), -k (column/field)

# Initialize an empty array to store numbers
numbers=()

# Loop to take 10 numbers from the user
for i in {1..10}; do
  # Prompt the user to enter number i
  read -p "Enter number $i: " num
  # Add the number to the array
  numbers+=($num)
done

# Ask the user which sort option they want
echo "Choose a sort option:"
echo "-r (reverse order)"
echo "-u (unique values only)"
echo "-k (sort by column/field)"

# Store user choice in variable "option"
read option

# Print each number on a new line and sort based on user input
# printf "%s\n" prints each array element on its own line
# sort $option applies the option the user chose
printf "%s\n" "${numbers[@]}" | sort $option
