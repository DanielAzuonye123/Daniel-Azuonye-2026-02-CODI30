#!/bin/bash

# =========================
# QUOTATIONS IN BASH
# =========================

# What are quotes?
# Quotes control how Bash interprets text and variables.

# =========================
# DOUBLE QUOTES " "
# =========================
# Variables work inside double quotes

name="Daniel"
echo "Hello $name"

# Output: Hello Daniel

# =========================
# SINGLE QUOTES ' '
# =========================
# Variables do NOT work inside single quotes

echo 'Hello $name'

# Output: Hello $name

# =========================
# NO QUOTES
# =========================
# Works only for simple text (not safe with spaces)

echo Hello Daniel

# =========================
# COMMON MISTAKES
# =========================
# - Using single quotes when variables are needed
# - Forgetting quotes when text has spaces
# - Expecting variables to work inside single quotes

# =========================
# TROUBLESHOOTING
# =========================
# If variables don’t show:
# → You are using single quotes instead of double quotes
