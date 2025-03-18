#!/bin/bash

# Function to check for Python 3 installation
check_python() {
    if ! command -v python3 &> /dev/null; then
        echo "Python3 is not installed. Please install it to run the game."
        exit 1
    fi
}

# Check for Python 3
check_python

# Enable Virtual ENV
. venv.sh

# Play Game
python3 main.py
