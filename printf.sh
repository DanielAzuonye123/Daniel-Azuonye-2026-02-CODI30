#!/bin/bash

# =========================
# PRINTF IN BASH
# =========================

# What is printf?
# printf is used to format and print output more precisely than echo.

# =========================
# BASIC USAGE
# =========================

printf "Hello World\n"

# \n means new line

# =========================
# USING VARIABLES
# =========================

name="Daniel"
printf "My name is %s\n" "$name"

# %s is a placeholder for a string

# =========================
# MULTIPLE VALUES
# =========================

age=16
printf "Name: %s Age: %d\n" "$name" "$age"

# %d is used for numbers

# =========================
# COMMON MISTAKES
# =========================
# - Forgetting \n (everything prints on one line)
# - Not using placeholders properly
# - Missing quotes around variables

# =========================
# TROUBLESHOOTING
# =========================
# If output looks wrong:
# - Check placeholders (%s, %d)
# - Check number of variables matches placeholders
