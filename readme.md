# Local Setup

You should use a virtual Environment so your python packages are the same version as the project and limited to only the 
packages we need. Pycharm has this built in with venv.

Install PostgreSQL and libpq. These are used in the Heroku deployed environment and some dependencies in `requirements.txt` need them. You can continue to use sqlite3 for local development.
* https://www.postgresql.org/download/
* https://www.psycopg.org/docs/install.html#prerequisites

Navigate your terminal to the project root directory.

Install package from the `requirements.txt` file with
`pip install -r requirements.txt`

Generate/update your local DB with `python manage.py migrate`

You should see a `db.sqlite3` file in the project root directory now.

## Local Environment config variables
Create a file in your project root named `.env` using the `.env-template` file.

This file will hold all the configuration variables as well as sensitive variables we don't want to publish on a 
public Github repository. 


## Start the server

Verify everything is working with the command `python manage.py runserver` 

The server address should show in the terminal which is http://127.0.0.1:8000/ or http://localhost:8000/ by default.

## Updating Packages

If you have to install new packages or update existing packages `requirements.txt` needs to be updated. 

Running the command `pip freeze > requirements.txt` will dump your installed packages to the `requirements.txt` file.
It's important to be using a Virtual Environment so that you only dump the packages used for this project and not all 
the global packages installed on your machine.
Animal Adoption
