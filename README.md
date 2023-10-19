# T1A3 - Terminal Application

## Git Repository
[Repository link: https://github.com/dtbooy/DirkBooy-T1A3-TerminalApplication](https://github.com/dtbooy/DirkBooy-T1A3-TerminalApplication)



## Key Features
The Terminal Application for this project will be a simple terminal based quiz application. It will 
* allow users to take a 10 question quiz multiple choice quiz 
* allow users to add/remove questions and topics for future quizzes
* have a menu to allow navigation and choice selection within the application
* have an in-app help function that will give instruction on how to use the app
* have scripts written to assist installation and application launch
* have gone through testing to ensure app functionallity and stability

### Quiz functionality
For each quiz: 
1. the user will be able to select a topic, 
1. the application will select a 10 multiple choice questions from the saved questions file for that topic. 
1. Each question will be printed to the terminal and requested an answer to user. 
1. User input will be validated to ensure it is a valid selection: either alpha ("A", "B", "C", or "D") or numeric (1, 2, 3, 4) 
1. The correct answer will be revealed and the user will be given feedback. then the next question will be displayed
1. At the end of the quiz, the users score will be displayed 

Optional functionallity may be added to the quiz function if time allows, including:
* adding a limit time to answer the question, 
* Update scoring mechanism to allow faster answers to give more score

### Quiz edit functionality
Will allow users to delete or add their own questions to the selected topic. changes will be saved to file.
New topic will save a new quiz file - user will need to add at least 10 questions to add a new topic.


### Application navigation
Navigation chains for the program will be as follows:
* New quiz
    * Topic selection --> start quiz
* Edit quiz
    * Add new quiz topic --> start new quiz & question add function
    * edit existing
        * select topic
            * add question --> add question function
            * remove question --> remove question 
* Help
    * How to play --> displays help topic
    * How to edit --> displays help topic
* Quit --> terminates program

### Product Testing
An automated testing reigeme will be developed

### Installation & App launch scripts
Scripts will be developed to simplify the installation and application launch for the user

#### Launch script
Launch script will 
* check Python3 is installed on the machine
* will default to launch into quiz taking mode but will take an argv to launch into quiz edit mode 

### Install script
Install script will:
* check for python3 installation
    * if no install is detected it will halt and display a instuctions to the user on how to install python3
* will make a directory structure to store .py scripts, quiz files, requirements.txt, etc
* will install any required python packages in requirements.txt 
* link to launch script added to desktop (on request)

## Implementation Plan
An implementation plan has been developed for this project in MS Planner.
To view the to implementation plan on MS Planner follow this link: [https://tasks.office.com/coderacademy.edu.au/Home/PlanViews/MN5oAS6OQkuomEOswzAJbQgAGgfe?Type=PlanLink&Channel=Link&CreatedTime=638332964113580000](https://tasks.office.com/coderacademy.edu.au/Home/PlanViews/MN5oAS6OQkuomEOswzAJbQgAGgfe?Type=PlanLink&Channel=Link&CreatedTime=638332964113580000)

The features have been broken down into component cards, each has been assigned a priority and a planned completion date. As the project matures the prioirities and forecast completion dates of individual elements will change.

### Screenshots of plan over course of project
19 October 2023: 
![2023/10/19 Project Board](./docs/20231019-board.png)
![2023/10/19 Project Status Chart](./docs/20231019-chart.png)
![2023/10/19 My cards Status](./docs/20231019-mytasks.png)
20 October 2023:
21 October 2023:
22 October 2023:
23 October 2023:
24 October 2023:
25 October 2023:
26 October 2023:


## Help Documentation

### Installation

### Requirements

### Startup

### How to quiz!

### Editing quizzes

#### Add remove questions from a topic

### Make your own quizes


## Style Guide
Style Guide used python code in this project is [PEP 8](https://peps.python.org/pep-0008/)

## References