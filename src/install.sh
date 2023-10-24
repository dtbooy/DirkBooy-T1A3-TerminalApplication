#!/bin/bash


#1. check if python3.10+ installed - if not then exit
if ! [ "python3 -c 'import sys; print(sys.version_info[0])' == 3" ] && [ "python3 -c 'import sys; print(sys.version_info[1:1])' -gt 10" ]
then
    echo 'Python3.10+ required to play. Dowload for free at https://www.python.org/downloads/' 
    exit
fi

#2. copy files to ~/quiz folder

# Check if the directory ~/quiz exists so we don't overwrite
if [ -d ~/quiz ]; 
then
  echo "Directory ~/quiz exists. Delete or rename directory to install quiz"
else
#make a directory for the application
    mkdir ~/quiz/
#Copy files to 
    cp ./src/main.py ~/quiz
    cp ./src/file_handling.py ~/quiz
    cp ./src/playquiz.py ~/quiz
    cp -r ./src/quiz_data ~/quiz
    cp ./src/quiz.sh ~/quiz
    cp ./src/requirements.txt ~/quiz
fi

#3. install venv in quiz folder
echo "Installing Pyhton virtual environment"
cd ~/quiz
python3 -m venv .venv
source .venv/bin/activate

#4. install required packages from requirements.txt
echo "Installing required packages from requirements.txt"
pip install -r requirements.txt
