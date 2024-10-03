"""A collection of scripts to manage the dev environment."""

from .code_scripts import format, lint, typecheck
from .django_scripts import (
    collectstatic,
    createsuperuser,
    makemigrations,
    migrate,
    runserver,
)
from .sphinx_scripts import genapidocs, makedocs

__all__ = [
    "format",
    "lint",
    "typecheck",
    "runserver",
    "makemigrations",
    "migrate",
    "createsuperuser",
    "collectstatic",
    "makedocs",
    "genapidocs",
]
