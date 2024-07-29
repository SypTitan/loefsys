import subprocess


def runserver():
    subprocess.run(["poetry", "run", "manage.py", "runserver"], check=False)


def makemigrations():
    subprocess.run(["poetry", "run", "manage.py", "makemigrations"], check=False)


def migrate():
    subprocess.run(["poetry", "run", "manage.py", "migrate"], check=False)


def createsuperuser():
    subprocess.run(["poetry", "run", "manage.py", "createsuperuser"], check=False)


def collectstatic():
    subprocess.run(["poetry", "run", "manage.py", "collectstatic"], check=False)
