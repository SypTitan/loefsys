loefsys.scripts.django_scripts
==============================

.. py:module:: loefsys.scripts.django_scripts

.. autoapi-nested-parse::

   Submodule containing scripts related to Django.

   With the available functions, several django-admin functions are accessible.



Functions
---------

.. autoapisummary::

   loefsys.scripts.django_scripts.runserver
   loefsys.scripts.django_scripts.makemigrations
   loefsys.scripts.django_scripts.migrate
   loefsys.scripts.django_scripts.createsuperuser
   loefsys.scripts.django_scripts.collectstatic


Module Contents
---------------

.. py:function:: runserver() -> None

   Boot up Django's development webserver.

   See :djadmin:`django:runserver` for more details.


.. py:function:: makemigrations() -> None

   Make migrations based on the changes in the code.

   See :djadmin:`django:makemigrations` for more details.


.. py:function:: migrate() -> None

   Apply migrations to the database.

   See :djadmin:`django:migrate` for more details.


.. py:function:: createsuperuser() -> None

   Create an admin user for the database.

   See :djadmin:`django:createsuperuser` for more details.


.. py:function:: collectstatic() -> None

   Collect all static files in the ``static`` folder.

   See :djadmin:`django:collectstatic` for more details.


