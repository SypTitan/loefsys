Getting Started
===============
On this page, you will find instructions on how to set up your coding environment to contribute to the project.

Prerequisites
-------------
In order to contribute to the project, you should have the following prerequisites:

* Install `Git <https://git-scm.com/>`_.
* Ensure you have Python 3.12 installed or higher. You can check which version you are running by executing the following command in your terminal::

    $ python --version

* Install `Poetry <https://python-poetry.org/>`_ by running one of the following commands in your terminal, depending on your OS:

    * For Linux, macOS, Windows (WSL)::

        $ curl -sSL https://install.python-poetry.org | python3 -

    * For Windows (Powershell)::

        $ (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -

* Clone the repository locally by executing the following command::

    $ git clone https://github.com/Loefbijter/loefsys.git

* Then, open the directory with the cloned repository and execute::

    $ poetry install

* Install all pre-commit hooks with the following command::

    $ pre-commit install  # If pre-commit isn't recognized, use this:
    $ poetry run pre-commit install

* In the root directory, make a ``.env`` file and fill it with the necessary environment variables. In :ref:`recommended-env`, the recommended environment variables for development can be found.
* Finally, you can start the development server with::

    $ poetry run runserver

Available commands
------------------

* ``poetry run runserver``

    Boot up Django's development webserver. See `runserver <https://docs.djangoproject.com/en/5.0/ref/django-admin/#runserver>`_ for more details.
* ``poetry run makemigrations``

    Make migrations based on the changes in the code. See `makemigrations <https://docs.djangoproject.com/en/5.0/ref/django-admin/#makemigrations>`_ for more details.

* ``poetry run migrate``

    Apply migrations to the local database. See `migrate <https://docs.djangoproject.com/en/5.0/ref/django-admin/#migrate>`_ for more details.

* ``poetry run createsuperuser``

    Creates an admin user for the local database. See `createsuperuser <https://docs.djangoproject.com/en/5.0/ref/django-admin/#createsuperuser>`_ for more details.

* ``poetry run collectstatic``

    Collects all static files in the ``static`` folder. See `collectstatic <https://docs.djangoproject.com/en/5.0/ref/django-admin/#collectstatic>`_ for more details.

* ``poetry run docs``

    Generate HTML documentation. See `sphinx-build <https://www.sphinx-doc.org/en/master/man/sphinx-build.html>`_ for more details.

* ``poetry run apidocs``

    Generates API docs from docstrings in the code. See `sphinx-apidoc <https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html>`_ for more details.
