# MTX Simple App
This is a simple app where users can sign up and sign in from a landing page into a dashboard. It provides options to sign up with email and password, sign in with Google, and sign in with Facebook. Inside the dashboard, user can see the profile, change name, change password, see the user list and statistic.

## Requirements
* Python 3.9.9
* Poetry
* Postgresql

## Installation
* Download and install PostgreSQL database [Read more...](https://www.postgresql.org/)
* Create a new database for the app
* Install python Poetry as the dependency manager [Read more...](https://python-poetry.org/docs/#installation)
* Clone the repository `git clone https://github.com/Krisnadi/mtx-simple-app.git`
* Change directory to app root folder `cd mtx-simple-app/`
* Create poetry virtual environment and install the project dependencies with `poetry install` and activate it with `poetry shell` [Read more...](https://python-poetry.org/docs/basic-usage/)
* Create an .env file by copying the template `cp .env.dist .env` and change the .env content
* Run the database migration with `python manage.py migrate`

## Run Development Server
* Run the app with `python manage.py runserver`
* To access the app, open [localhost:8000](http://localhost:8000) on browser

## Testing
To run the test case, execute `python manage.py test`

## API Documentation
The API documentation for all the endpoints are listed [here](https://documenter.getpostman.com/view/2027606/UVXetdxd)

## Demo App
You can access the demo app [here](https://mtx-simple-app.herokuapp.com/)

## App Structure
```
├── auth
│   ├── adapter.py
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── models.py
│   ├── registration
│   │   ├── urls.py
│   │   └── views.py
│   ├── tests.py
│   ├── urls.py
│   ├── validators.py
│   └── views.py
├── .env
├── .env.dist
├── frontsite
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── .gitignore
├── manage.py
├── mysite
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── poetry.lock
├── Procfile
├── pyproject.toml
├── README.md
└── templates
    ├── dashboard.html
    ├── email_verification.html
    ├── home.html
    └── signup.html
└── user
    ├── admin.py
    ├── apps.py
    ├── __init__.py
    ├── middleware.py
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── __init__.py
    ├── models.py
    ├── serializers.py
    ├── tests.py
    ├── urls.py
    └── views.py
```
* **auth**: Contains authentication related API
* **.env**: The environment file, contains project configurations
* **.env.dist**: Template for .env file
* **frontsite**: Contains routes for the front website template
* **mysite**: The project core folder, it contains the project settings and routes
* **poetry.lock**: File to lock the dependencies version for the project
* **Procfile**: File used for Heroku deployment [Read more...](https://devcenter.heroku.com/articles/procfile)
* **pyproject.toml**: Contains the project dependencies used by Poetry package manager
* **templates**: Contains the html templates of the app
* **user**: Contains user list and statistic api
