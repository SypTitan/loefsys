Getting Started
===============
On this page, you will find instructions on how to set up your coding environment to contribute to the project.

Prerequisites
-------------
In order to contribute to the project, you should have the following prerequisites:

#. Install `Git <https://git-scm.com/>`_.
#. Ensure you have Python 3.12 installed or higher. You can check which version you are running by executing the following command in your terminal::

    $ python --version

#. Install `Poetry <https://python-poetry.org/>`_ by following the installation instructions `here <https://python-poetry.org/docs/#installation>`_.
#. Clone the repository locally by executing the following command::

    $ git clone https://github.com/Loefbijter/loefsys.git

#. Then, open the directory with the cloned repository and execute::

    $ poetry install

#. Install all pre-commit hooks with the following command::

    $ pre-commit install  # If pre-commit isn't recognized, use this:
    $ poetry run pre-commit install

#. In the root directory, make a ``.env`` file and fill it with the necessary environment variables. In :ref:`recommended-env`, the recommended environment variables for development can be found.
#. Finally, you can start the development server with::

    $ poetry run runserver

#. Now, head over to `localhost:8000 <localhost:8000>` in your browser and you should see the homepage of loefsys.

Creating a Superuser
^^^^^^^^^^^^^^^^^^^^

#. If you want to create an admin user for yourself in your local database, you can run the following command::

    $ poetry run createsuperuser

    # You will be asked to enter a username, email address, and password. Choose these as you like. You can keep the email address field empty.
    # If you get a prompt that your password is too weak, you can ignore this (only in development of course, we don't do weak passwords in production ;)).

#. You just created your first superuser! Head over to http://localhost:8000/accounts/login/ and log in with the credential which you have entered in the previous step.

Available Commands
------------------

* ``poetry run runserver``

    Boot up Django's development webserver. See `runserver <https://docs.djangoproject.com/en/5.0/ref/django-admin/#runserver>`_ for more details.
* ``poetry run makemigrations``

    Make migrations based on the changes in the code. See `makemigrations <https://docs.djangoproject.com/en/5.0/ref/django-admin/#makemigrations>`_ for more details.

* ``poetry run migrate``

    Apply migrations to the local database. See `migrate <https://docs.djangoproject.com/en/5.0/ref/django-admin/#migrate>`_ for more details.

* ``poetry run createsuperuser``

    Create an admin user for the local database. See `createsuperuser <https://docs.djangoproject.com/en/5.0/ref/django-admin/#createsuperuser>`_ for more details.

* ``poetry run collectstatic``

    Collect all static files in the ``static`` folder. See `collectstatic <https://docs.djangoproject.com/en/5.0/ref/django-admin/#collectstatic>`_ for more details.

* ``poetry run docs``

    Generate HTML documentation. See `sphinx-build <https://www.sphinx-doc.org/en/master/man/sphinx-build.html>`_ for more details.

* ``poetry run apidocs``

    Generate API docs from docstrings in the code. See `sphinx-apidoc <https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html>`_ for more details.

* ``mypy``

    Run `mypy <https://mypy.readthedocs.io/en/latest/>`_ type checking on the code.
