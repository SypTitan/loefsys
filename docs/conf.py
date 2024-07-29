"""Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

import os
import sys
from pathlib import Path

import django

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Loefsys"
copyright = "2024, Loefbijter Webcie"  # noqa: A001
author = "Loefbijter Webcie"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

sys.path.insert(1, str(Path(__file__).parent / "_ext"))
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "djangodocs",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

nitpicky = True


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# -- Options for Intersphinx -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "django": (
        "https://docs.djangoproject.com/en/5.0/",
        "https://docs.djangoproject.com/en/dev/_objects/",
    ),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
    "mypy": ("https://mypy.readthedocs.io/en/latest/", None),
}

# -- Options for Autodoc -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html

autodoc_typehints = "both"
autodoc_member_order = "groupwise"

# -- Options for Napoleon ----------------------------------------------------

napoleon_preprocess_types = True
napoleon_type_aliases = {
    "django.db.models.base.Model": "test",
    "QuerySet": ":class:`~django:django.db.models.query.QuerySet`",
    "datetime": ":class:`~python:datetime.datetime`",
}

# -- Options for Django configuration ----------------------------------------

sys.path.insert(0, str(Path(__file__).resolve(strict=True).parent.parent))
os.environ["DJANGO_SETTINGS_MODULE"] = "loefsys.settings"
django.setup()
