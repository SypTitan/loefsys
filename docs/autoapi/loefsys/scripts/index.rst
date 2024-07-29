loefsys.scripts
===============

.. py:module:: loefsys.scripts

.. autoapi-nested-parse::

   A collection of scripts to manage the dev environment.



Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/loefsys/scripts/code_scripts/index
   /autoapi/loefsys/scripts/django_scripts/index
   /autoapi/loefsys/scripts/sphinx_scripts/index


Functions
---------

.. autoapisummary::

   loefsys.scripts.format
   loefsys.scripts.lint
   loefsys.scripts.typecheck
   loefsys.scripts.collectstatic
   loefsys.scripts.createsuperuser
   loefsys.scripts.makemigrations
   loefsys.scripts.migrate
   loefsys.scripts.runserver
   loefsys.scripts.makedocs
   loefsys.scripts.genapidocs


Package Contents
----------------

.. py:function:: format() -> None

   Apply formatting to the project code.

   See `Ruff formatter <https://docs.astral.sh/ruff/formatter/>`_ for more details.


.. py:function:: lint() -> None

   Apply linting to the project code.

   See `Ruff linter <https://docs.astral.sh/ruff/linter/>`_ for more details.


.. py:function:: typecheck() -> None

   Perform typechecking analysis on the project code.

   See :doc:`mypy <mypy:index>` for more details


.. py:function:: collectstatic() -> None

   Collect all static files in the ``static`` folder.

   See :djadmin:`django:collectstatic` for more details.


.. py:function:: createsuperuser() -> None

   Create an admin user for the database.

   See :djadmin:`django:createsuperuser` for more details.


.. py:function:: makemigrations() -> None

   Make migrations based on the changes in the code.

   See :djadmin:`django:makemigrations` for more details.


.. py:function:: migrate() -> None

   Apply migrations to the database.

   See :djadmin:`django:migrate` for more details.


.. py:function:: runserver() -> None

   Boot up Django's development webserver.

   See :djadmin:`django:runserver` for more details.


.. py:function:: makedocs() -> None

   Generate HTML documentation for the project.

   See :doc:`sphinx:man/sphinx-build` for more details.


.. py:function:: genapidocs() -> None

   Generate API documentation from the docstrings.

   See :doc:`sphinx:man/sphinx-apidoc` for more details.


