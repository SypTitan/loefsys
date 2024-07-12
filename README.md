# Loefbijter System (LoefSys)

This repository is owned by the Nijmeegse student sailing association (N.S.Z.V.) De Loefbijter. The code in this repository facilitates the internal systems of De Loefbijter like our website, mobile app and (in the future) user management system.

Any questions related to this repository should be directed towards the [website committee](mailto:webcie@loefbijter.nl).

This project uses the [Zappa](https://github.com/Miserlou/Zappa) and [Django](https://github.com/django/django) frameworks.

License: MIT

## Getting started
### Prerequisites
You should have
- The repository cloned locally, if you don't have this yet execute the command:

        git clone https://github.com/Loefbijter/loefsys.git
- Python version 3.12 installed or higher
- An installation of [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer).
    - For Linux, macOS, Windows (WSL):

            curl -sSL https://install.python-poetry.org | python3 -
    - For Windows (Powershell):

            (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
- Command line
- Development environment (PyCharm or VSCode recommended)

### Setting up your environment
1. Copy the file `infra/.env.example` to the root directory of the project and rename it to `.env`.
2. Open the terminal in the root directory of the project and run the following in your command line:

        poetry update
3. Finally, enable pre-commit by running the following command:

        pre-commit install
4. Setting up the development environment is now finished. You can run the developmental webserver by running the following command:

        python manage.py runserver
5. Head over to [localhost:8000](localhost:8000) in your browser and you should see the homepage of loefsys.

Congrats! You successfully set up your environment. Don't forget to shut down the container when you're finished using `$ docker compose down` and repeat step 3 and 4 to return to your environment.

### Creating a local superuser
A superuser is an administrator of the system. Such a user is necessary to create new reservations, groups, users, etc. for testing purposes. If you haven't yet created a superuser you can create one now.
1. Make sure your environment is up and running, if not then follow the steps as described in the section 'Setting up your environment'.
2. Run the following command in your terminal and follow the steps to enter a username, email address, and passwords.

        python manage.py createsuperuser
   1. You will be asked to enter a username, email address, and password. Choose these as you like. You can keep the email address field empty.
   2. If you get a prompt that your password is too weak, you can ignore this (only in development of course, we don't do weak passwords in production ;)).

You just created your first superuser! Head over to http://localhost:8000/accounts/login/ and log in with the credential which you have entered in the previous step.

## Basic commands

### Type checks

Run type checks with mypy:

    mypy

### Running tests

Run tests with the built-in test runner:

    python manage.py test

## Deployment

TBD
