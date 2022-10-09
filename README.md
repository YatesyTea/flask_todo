# flask_todo

# Purpose of This Project
* To create a minimal project to refresh on my flask skills, alongside learning how to use SQLAlchemy for small scale projects.
* Potentially Dockerize the Project later on for Github Pages or AWS Deployment
* To test github actions pipelines for devwork later on down the line.

# Scope

Created by following this tutorial: https://www.youtube.com/watch?v=yKHJsLUENl0
To refresh on how Flask works as a framework alongside basic SQLAlchemy commands.

Styling will be done entirely without this video however.

File structure is largely simplified (won't use this way on larger projects) with a singular app.py that holds all the business logic.

Project developing as follows:

    1. Create Skeleton with Imports.
    2. Add basic data passthrough between app.py and base.html
    3. Create SQLite DB and use data passthrough.
    4. Add CRUD functionality.
    5. Style Components.

# Installation For Development

1. Clone Repo
2. python -m venv venv
3. '. venv/Scripts/activate' or '. venv/bin/activate' (Mac/Linux)
4 'pip install -r requirements.txt'
5 'python app.py runserver'
6 Should be open on [localhost:5000](http://localhost:5000/)
7 Should now be able to add and delete, and edit tasks.

