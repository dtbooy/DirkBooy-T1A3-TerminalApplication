#!/bin/bash
# 1. Check for python3
if ! [[ -x "$(command -v python3)" ]]
then
  echo 'Error: 
    This program requires Python3 to run, but it looks like Python3 is not installed on your system.
    For a guide to installing Python 3 see: https://docs.python-guide.org/starting/installation/' >&2
  exit 1
fi

# #2. install venv in quiz folder
# echo "Activating Python virtual environment"
# python3 -m venv .venv
# source .venv/bin/activate

# #3. install required packages from requirements.txt
# echo "Installing required packages from requirements.txt"
# pip install -r requirements.txt

# 4. Make sure quiz files are in read-write mode 
chmod 666 ./quiz_data/quiz_*

#5. Open the quiz program
python3 main.py

# #6. Deactivate virtual environment
# deactivate