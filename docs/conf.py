import os
import sys
from pathlib import Path

import django

# -- Initialize with Django --------------------------------------------------

sys.path.insert(0, str(Path(__file__).resolve(strict=True).parent.parent))
os.environ["DJANGO_SETTINGS_MODULE"] = "loefsys.settings"
django.setup()

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Loefsys"
copyright = "2024, Loefbijter Webcie"
author = "Loefbijter Webcie"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc", "sphinxcontrib.napoleon"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
