#!/bin/bash

# FUNCTIONS IN BASH
# A function is a reusable block of code
# It helps avoid repeating yourself

say_hello() {
  echo "Hello World"
}

say_hello

say_name() {
  echo "Hello $1"
}

say_name "Daniel"
