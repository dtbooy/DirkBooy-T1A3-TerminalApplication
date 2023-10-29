# T1A3 - Terminal Application

## Git Repository
[Repository link: https://github.com/dtbooy/DirkBooy-T1A3-TerminalApplication](https://github.com/dtbooy/DirkBooy-T1A3-TerminalApplication)
https://github.com/dtbooy/DirkBooy-T1A3-TerminalApplication/commits/main


## Key Features
The Terminal Application for this project will be a simple terminal based quiz application. It will 
* allow users to take a 10 question quiz multiple choice quiz 
* allow users to add/remove questions and topics for future quizzes
* have a menu to allow navigation and choice selection within the application
* have an in-app help function that will give instruction on how to use the app
* have scripts written to assist application launch
* have gone through testing to ensure app functionality and stability

### Quiz functionality
For each quiz: 
1. The user will be able to select a topic, 
1. The application will select a 10 multiple choice questions from the saved questions file for that topic. 
1. Each question will be printed to the terminal and requested an answer to user. 
1. User input will be validated to ensure it is a valid selection: either alpha ("A", "B", "C", or "D") or numeric (1, 2, 3 or 4) 
1. The correct answer will be revealed and the user will be given feedback. Then the next question will be displayed
1. At the end of the quiz, the users score will be displayed 

Optional functionality may be added to the quiz function if time allows, including:
* adding a limit time to answer the question, 
* Update scoring mechanism to allow faster answers to give more score

### Quiz edit functionality
Will allow users to delete or add their own questions to the selected topic. Changes will be saved to file.
New topic will save a new quiz file - user will need to add at least 10 questions to add a new topic.


### Application navigation
Navigation chains for the program will be as follows:
* Play quiz
    * Topic selection --> start quiz
* Edit quiz
    * edit existing
        * select topic
            * add question --> add question function
            * remove question --> remove question 
    * Add new quiz topic --> start new quiz & question add function
    * Delete a quiz --> delete quiz file
* Help
    * How to play --> displays help topic
    * How to Add a question to a quiz,--> displays help topic
    * How to Delete a question to a quiz,--> displays help topic
    * How to Create a new quiz,--> displays help topic
    * How to Delete a quiz,--> displays help topic
    * How to edit --> displays help topic
* Quit --> terminates program

### Product Testing
An automated testing regime will be developed

### Installation & App launch scripts
Scripts will be developed to simplify the installation and application launch for the user

#### Launch script
Launch script will 
* check Python3 is installed on the machine
* will default to launch into quiz taking mode but will take an argv to launch into quiz edit mode 

### Install script
Install script will:
* check for python3 installation
    * if no install is detected it will halt and display a instructions to the user on how to install python3
* will make a directory structure to store .py scripts, quiz files, requirements.txt, etc
* will install any required python packages in requirements.txt 
* link to launch script added to desktop (on request)

## Implementation Plan
An implementation plan has been developed for this project in MS Planner.
To view the implementation plan on MS Planner follow this link: [https://tasks.office.com/coderacademy.edu.au/Home/PlanViews/MN5oAS6OQkuomEOswzAJbQgAGgfe?Type=PlanLink&Channel=Link&CreatedTime=638332964113580000](https://tasks.office.com/coderacademy.edu.au/Home/PlanViews/MN5oAS6OQkuomEOswzAJbQgAGgfe?Type=PlanLink&Channel=Link&CreatedTime=638332964113580000).  

Alternatively an excel export of the MS Planner Workplan is in the docs folder here: [DirkBooy-T1A3-Workplan-export.pdf](./docs/DirkBooy-T1A3-Workplan-export.pdf)

The features have been broken down into component cards, each has been assigned a priority and a planned completion date. As the project matures the priorities and forecast completion dates of individual elements will change.

### Screenshots of plan over course of project
#### 19 October 2023: 
##### Project Board - 19 October 2023
![2023/10/19 Project Board](./docs/20231019-board.png)
##### Project Status Chart - 19 October 2023
![2023/10/19 Project Status Chart](./docs/20231019-chart.png)
##### Daily task cards - 19 October 2023
![2023/10/19 My cards Status](./docs/20231019-mytasks.png)
#### 20 October 2023:
##### Project Board - 20 October 2023
![2023/10/20 Project Board](./docs/20231020-board.png)
##### Project Status Chart - 20 October 2023
![2023/10/20 Project Status Chart](./docs/20231020-chart.png)
##### Daily task cards - 20 October 2023
![2023/10/20 My cards Status](./docs/20231020-mytasks.png)
#### 21 October 2023:
##### Project Board - 21 October 2023
![2023/10/21 Project Board](./docs/20231021-board.png)
##### Project Status Chart - 21 October 2023
![2023/10/21 Project Status Chart](./docs/20231021-chart.png)
##### Daily task cards - 21 October 2023
![2023/10/21 My cards Status](./docs/20231021-mytasks.png)
#### 22 October 2023:
##### Project Board - 22 October 2023
![2023/10/22 Project Board](./docs/20231022-board.png)
##### Project Status Chart - 22 October 2023
![2023/10/22 Project Status Chart](./docs/20231022-chart.png)
##### Daily task cards - 22 October 2023
![2023/10/22 My cards Status](./docs/20231022-mytasks.png)
#### 23 October 2023:
##### Project Board - 23 October 2023
![2023/10/23 Project Board](./docs/20231023-board.png)
##### Project Status Chart - 23 October 2023
![2023/10/23 Project Status Chart](./docs/20231023-chart.png)
##### Daily task cards - 23 October 2023
![2023/10/23 My cards Status](./docs/20231023-mytasks.png)
#### 24 October 2023:
##### Project Board - 24 October 2023
![2023/10/24 Project Board](./docs/20231024-board.png)
##### Project Status Chart - 24 October 2023
![2023/10/24 Project Status Chart](./docs/20231024-chart.png)
##### Daily task cards - 24 October 2023
![2023/10/24 My cards Status](./docs/20231024-mytasks.png)
#### 26 October 2023:
##### Project Board - 26 October 2023
![2023/10/26 Project Board](./docs/20231026-board.png)
##### Project Status Chart - 26 October 2023
![2023/10/26 Project Status Chart](./docs/20231026-chart.png)
##### Daily task cards - 26 October 2023
![2023/10/26 My cards Status](./docs/20231026-mytasks.png)
#### 29 October 2023:
##### Project Board - 29 October 2023
![2023/10/29 Project Board](./docs/20231029-board.png)
##### Project Status Chart - 29 October 2023
![2023/10/29 Project Status Chart](./docs/20231029-chart.png)
##### Daily task cards - 29 October 2023
![2023/10/29 My cards Status](./docs/20231029-mytasks.png)



## Help Documentation
### Requirements

#### Software requirements
Operating system:  
Recommended: Linux Ubuntu  
Windows users can install WSL with Ubuntu to run the application. For instruction installing WSL for windows, see: [https://learn.microsoft.com/en-us/windows/wsl/install](https://learn.microsoft.com/en-us/windows/wsl/install)

Other software:  
Python 3


#### Dependencies
* exceptiongroup==1.1.3
* iniconfig==2.0.0
* packaging==23.2
* pluggy==1.3.0
* PyInputPlus==0.2.12
* PySimpleValidate==0.2.12
* pytest==7.4.2
* stdiomask==0.0.6
* tomli==2.0.1

### Installation
Download the application files from [https://github.com/dtbooy/DirkBooy-T1A3-TerminalApplication/archive/refs/heads/main.zip](https://github.com/dtbooy/DirkBooy-T1A3-TerminalApplication/archive/refs/heads/main.zip). Unzip the files into your chosen directory. 

Ensure you have Python 3 installed on your machine. to check if Python3 is install on your machine, in the terminal tpye the command __Python3 -V__ if python is installed you will get the output of the version of python3 you have installed eg: Python 3.10.12. If you recieve an error such as "Python was not found" you will need to intall Python3 before running the application.

For instruction on installing python please visit: [https://docs.python-guide.org/starting/installation/](https://docs.python-guide.org/starting/installation/)

### Start-up
To start the program navigate to the src folder in the application folder and run the play.sh script (terminal command: ./play.sh). This script will:
1. Ensure python3 is installed 
2. Activate the application Virtual Environment (or create one for the first launch)
3. Install required packages from requirements.txt if not already installed.
4. Ensure sure quiz files are in read-write mode 
5. Open the quiz program
6. Deactivate virtual environment on close of the application 

### Menu navigation
The application can be navigated through a series of menus. To make a menu selection type the option number you would like to select and press enter.

### How to quiz!
To play a quiz select option __1. Play__ from the main menu. You will be presented with a list of the available quizzes. select the option number the quiz you would like to play to begin a round.  
A round will consist of 10 questions (or less if there are not 10 questions saved in the quiz file selected). Each question will be presented with 4 multiple choice answers. To select an answer type its corresponding letter and press enter (answers can be in upper or lower case). Alternatively you can use numbers instead of letters ie: 1 for A, 2 for B, 3 for C and 4 for D.  
Once you have submitted your answer, the correct answer will be revealed. You will receive points for correct answers and your total will be displayed at the end of the round.

Note: Questions are selected randomly from the pool of questions for the topic, and the order of the multiple choice answers is randomised each round. So every round should be different.

### Edit Mode
Quizzes are able to be edited in Edit mode. In this mode you can add or remove questions from a quiz, create a new quiz or delete a quiz.   

#### Add questions to a topic
To add a question to a quiz, from the Main menu select __2. Edit Mode__, then in the Edit Options select __1. Edit existing Quiz__. You will then be presented with the full list of available quizzes, select the number of the quiz you wish to edit, then select __1. Add Question__.   
The App will then guide you through the process of adding a question:
1. Add the Question
2. Add the _correct_ answer
3. Add an _incorrect_ answer 3 times
The question will then be displayed as it would in an actual quiz, with the correct answer indicated below. Confirm the details are correct and the question will be added to the quiz. 


#### Delete a question from a topic
To delete a question from a quiz, from the Main menu select __2. Edit Mode__, then in the Edit Options select __1. Edit existing Quiz__. You will then be presented with the full list of available quizzes, select the number of the quiz you wish to edit, then select __2. Delete Question__.  
The list of questions in the quiz will be displayed, select the number of the quiz you wish to delete, you will then be asked to confirm the correct question was selected. On confirmation the question will be deleted.  
__NOTE: this action is permanent and cannot be undone.__

#### Make your own quizzes
To make a new quiz; from the Main menu select __2. Edit Mode__, then in the Edit Options select __2. Create New Quiz__. You will then be prompted to enter the title of the new quiz.  
Note: the title must not be the same as an existing quiz and cannot contain special characters.  
The application will then guide the user through entering new questions:
1. Add the Question
2. Add the _correct_ answer
3. Add an _incorrect_ answer 3 times
The question will then be displayed as it would in an actual quiz, with the correct answer indicated below. Confirm the details are correct and the question will be added to the quiz. You will then be prompted to whether you want to add another question. Once you have entered all the questions select __No__ and the quiz will be saved.

The quiz files are saved a csv files. Quiz files can be added directly to the quiz_data folder located at ./src/quiz_data. The default quiz files can be found at: [https://github.com/dtbooy/DirkBooy-T1A3-TerminalApplication/tree/main/src/quiz_data](https://github.com/dtbooy/DirkBooy-T1A3-TerminalApplication/tree/main/src/quiz_data)

Quiz files can be created directly as csv files, with the headers:
* Question,
* Correct Answer,
* Wrong Answer 1,
* Wrong Answer 2,
* Wrong Answer 3  

Each question must have its own line and elements for each of the 5 columns. Filenames for quiz files must be in the form "quiz_[title_of_quiz].csv". For example the quiz __My First Quiz__ will be saved as __quiz_my_first_quiz.csv__.  

__NOTE: for best results you should add at least 20 questions to a new quiz__

#### Delete a quiz
To delete a quiz; from the Main menu select __2. Edit Mode__, then in the Edit Options select __3. Delete Quiz__. You will then be presented with the full list of available quizzes, select the number of the quiz you wish to delete. On confirmation the quiz will be deleted.  

__NOTE: This action is permanent and cannot be undone.__


## Style Guide
Style Guide used python code in this project is [PEP 8](https://peps.python.org/pep-0008/)

## References
PEP8
van Rossum, G., Warsaw, B. and Coghlan, N. (2001). PEP 8 – Style Guide for Python Code | peps.python.org. [online] peps.python.org. Available at: https://peps.python.org/pep-0008/.

PyInputPlus Documentation
Sweigart, A. (2023). PyInputPlus. [online] GitHub. Available at: https://github.com/asweigart/pyinputplus#readme [Accessed 29 Oct. 2023].

PyTest Documentation
docs.pytest.org. (n.d.). Full pytest documentation — pytest documentation. [online] Available at: https://docs.pytest.org/en/7.1.x/contents.html.



## Checklist -  Documentation
| R | Description | Done |
| - | - | - |
| R1 | Answers to all the documentation requirements below. |  |
| R2 | Your README.md should have a separate heading for each documentation requirement and answers organised under the appropriate headings. | Y |
| R3 | Provide full attribution to referenced sources (where applicable). |  |
| R4 | Provide a link to your source control repository | Y |
| R5 | Identify any code style guide. | Y |
| R6 | Develop a list of features that will be included in the application. | Y |
| R7 | Develop an implementation Plan | Y |
| R8 | Design help documentation, inc use and installation |  |


