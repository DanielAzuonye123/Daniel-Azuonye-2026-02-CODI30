#!/bin/bash

# =========================
# VARIABLES IN BASH
# =========================

# What is a variable?
# A variable stores data (text or numbers) for reuse in a script.
# Think of it like a labeled box that holds information.

# =========================
# HOW VARIABLES WORK
# =========================

# You assign a value using the = sign

# IMPORTANT RULE:
# There must be NO spaces around =

# ✔ Correct:
name="Daniel"

# ❌ Wrong:
# name = "Daniel"

# Why?
# Bash interprets spaces as separate commands, which causes errors.

# =========================
# USING VARIABLES
# =========================

name="Daniel"
age=16

# To DISPLAY a variable, use $

echo "My name is $name"
echo "My age is $age"

# $name means: replace this with the value stored in "name"

# =========================
# OUTPUT EXAMPLE
# =========================
# My name is Daniel
# My age is 16

# =========================
# COMMON MISTAKES
# =========================

# ❌ Forgetting $
# echo "My name is name"   (wrong)

# ❌ Adding spaces around =
# name = "Daniel"

# ❌ Misspelling variable names
# namee="Daniel"

# =========================
# TROUBLESHOOTING
# =========================

# If your script does not work:
# - Check that you used $ when calling variables
# - Check spelling carefully
# - Ensure no spaces around =
