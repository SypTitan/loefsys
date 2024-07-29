import subprocess


def lint():
    subprocess.run(["ruff", "check"])


def format():
    subprocess.run(["ruff", "format"])


def typecheck():
    subprocess.run(["mypy"])
