[![Build Status](https://travis-ci.org/AduweSandra/Shoppinglist.svg?branch=master)](https://travis-ci.org/AduweSandra/Shoppinglist)

# Shoppinglist
This is an application which enables users to create a shopping list for the several items they want to buy.

# Features

The application has several features as mentioned below:-

-A user is able to Register and get an account in the app
-A user is able to Login into the app using their credentials already supplied
-A user is able to create, edit, update and delete shopping lists
-A user is also able to create, edit, update and delete shopping list Items

# Setup

To start using this application, first clone it to your local machine by running

git clone https://github.com/AduweSandra/Shoppinglist.git
cd Shoppinglist
Create the virtual environment and activate it

virtualenv env
source env/bin/activate
Then install all the required dependencies

pip install -r requirements.txt
Then run the application

python run.py
To now view the application head over to

http://127.0.0.1:5000/

# UML

The application also has a UML diagram. For the structure of the app check it  here

# Testing

You can then run the application tests using

cd Shoppinglist
nosetests tests
