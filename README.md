# django_calendar
The goal of the project is to demonstrate the backend functions of a Calendar-like Web application implemented through DJANGO. 

The project folder is web_project and the app is named 'backend'
This project shows the CRUD operations of Scheduled Events in a Calendar. The API has been restricted by user authentication. 
The front end is kept as simple as possible and can be further built up.

## How to Use:
Follow the link: https://pacific-hamlet-44649.herokuapp.com/backend/

## Main Page:
You are given 2 options: Either to Login(Existing User) or Register(Create new user). They lead to the corresponding pages.

## Login Page: 
Login using existing credentials and the user id gets activated.

## Register:
Sign up using a username, email and password. After successful registering, go back to login page and login using the credentials and generates a unique Authentication id for each user.

## Dashboard:
The Calendar page shows up and allows 4 operations:
Create, Update, View, Delete Events 

## Create Event:
Allows you to create an event with title and date. The foreign key will be set to the current user thereby marking the event belonging to that user. 
The POST request makes a new entry of the model Event and sets attributes title, date and current user.

## View:
Lists all events of that user 
The GET request fetches all Events(filter) and returns an array of all events with foreign key=current user and displays on the screen

## Update/Delete:
Allows you to search using the title of the event and then Update/Delete the event.

## About the Database:
I have used db.sqlite3 database which can be easily viewed using django administration url.
There are 2 Models:
   Profile: Keeps a record of the user- his Username, Email, a unique User ID for authentication 
   Events: A record of all events with attributes- Title, date and foreign key=profile (i.e the current user)
 POST/GET Methods are used frequently here to interact with the database. 
 
 The project is deployed using heroku.
