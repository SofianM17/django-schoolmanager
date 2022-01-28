# Study Management System

## Table of Contents
1. [Technologies](#technologies)
2. [Installation](#installation)
3. [Getting Started](#getting-started)

## Technologies

- Python 3.10.0
- Django 3.2.9
- django-crispy-forms 1.13.0
- django-registration 3.2
- djangorestframework 3.12.4

- asgiref 3.4.1
- certifi 2021.10.8
- charset-normalizer 2.0.7
- confusable-homoglyphs 3.2.0
- idna 3.3
- pytz 2021.3
- requests 2.26.0
- sqlparse 0.4.2
- typing-extensions 3.10.0.2
- urllib3 1.26.7

## Installation

1. Clone the repository
```
$ git clone https://github.com/SofianM17/django-schoolmanager
```

2. Make sure required stacks are installed by running the command ```$ pip freeze```, which provides a list of currently installed packages. If not, install the required packages using the following commands:
```
$ python -m pip install Django
$ pip install django-crispy-forms
$ pip install django-registration
$ pip install djangorestframework
```
If any technologies are still missing refer to [Technologies](#technologies) and run ```pip install``` for the rest.

3. Navigate to
```
$ cd ../django-schoolmanager/schoolmanager
```

4. To run the program
```
$ python manage.py runserver
```

5. Navigate to the locally hosted server using the link provided by the CLI.

## Getting Started

### Registration/Login
To begin using the Study Management System, the user must register for an account by clicking on the “Register” button. The user will fill out the required fields to create an account followed by picking one of the account types. The difference between the student and instructor account is that the student may track extra information such as clubs, events, and finances which is not relevant to the use case of the instructor. 

### Navigating the System
Once an account is created, the user may login to view their dashboard. On the left is a navigation bar that the user can use to view different pages. Using the buttons with the plus symbol, the user may add classes, tasks, or events on their respective pages. Clicking this button will redirect the user to a form page with fields to fill out. Once the user completes filling this out, they must click the “Submit” button to display the information on their main page. Each information group is contained within a box (tile) with edit and delete icons. The user may edit the information or delete it as they wish. Editing information is similar to adding information, that is, the user will edit the fields to change any information then click “Submit” to display it. When deleting information, the user will be prompted with a confirmation before deleting. For the finance page, the user can add their initial expenses using the plus button. Once the information has been added, the user may edit their earnings and expenses using the plus and minus buttons. The calculation of the total value will be reflected each time the value changes. The finances may also be deleted to restart all the information rather than having to update everything.

## Demo
![Login and Registration Gif](https://i.gyazo.com/7bc1bee468c4d6191b2988f0607f6c19.gif)
![Add Class Gif](https://i.gyazo.com/08e456e82f8086094436d10148a8825e.gif)
![Update information Gif](https://i.gyazo.com/39c15c5dd76e4501f2f44d26717484bd.gif)
![Delete Information](https://i.gyazo.com/4e560b3dd00ae9d590757de5d26b8c15.gif)
