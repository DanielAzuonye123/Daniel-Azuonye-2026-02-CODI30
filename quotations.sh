#!/bin/bash

# quotations.sh
# Prints a random quote

echo "Here is a quote for you:"

quotes=(
"With great power comes great responsibility."
"Stay hungry, stay foolish."
"Knowledge is power."
"The only limit is your mind."
"Success is not final, failure is not fatal."
)

# Get random index
index=$((RANDOM % ${#quotes[@]}))

# Print random quote
echo "${quotes[$index]}"
