#!/bin/bash

# =========================
# FUNCTIONS IN BASH
# =========================
# A function is a reusable block of code.
# It helps avoid repeating yourself.

# Simple function
say_hello() {
    echo "Hello World"
}

say_hello

# Function with parameter
say_name() {
    echo "Hello $1"
}

say_name "Daniel"
