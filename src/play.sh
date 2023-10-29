#!/bin/bash
# 1. Check for python3
echo Checking for Python3...
if ! [[ -x "$(command -v python3)" ]]
then
  echo 'Error: 
    This program requires Python3 to run, but it looks like Python3 is not installed on your system.
    For a guide to installing Python 3 see: https://docs.python-guide.org/starting/installation/' >&2
  exit 1
fi
echo Done!

# #2. Activate venv in quiz folder
echo "Activating Python virtual environment"
python3 -m venv .venv
source .venv/bin/activate
echo Done!

# #3. install required packages from requirements.txt
echo "Checking for required packages from requirements.txt"
python3 -m pip install -r requirements.txt
echo Done!

# 4. Make sure quiz files are in read-write mode 
echo Checking 
chmod 666 ./quiz_data/quiz_*

#5. Open the quiz program
echo Opening Application
python3 main.py

# #6. Deactivate virtual environment
echo Deactivating Virtual Environment...
deactivate
echo Done!
echo Play again soon!
