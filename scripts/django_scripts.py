import subprocess

def runserver():
    subprocess.run(["poetry", "run", "manage.py", "runserver"])

def makemigrations():
    subprocess.run(["poetry", "run", "manage.py", "makemigrations"])

def migrate():
    subprocess.run(["poetry", "run", "manage.py", "migrate"])

def createsuperuser():
    subprocess.run(["poetry", "run", "manage.py", "createsuperuser"])

def collectstatic():
    subprocess.run(["poetry", "run", "manage.py", "collectstatic"])