loefsys.users.managers
======================

.. py:module:: loefsys.users.managers


Classes
-------

.. autoapisummary::

   loefsys.users.managers.UserManager


Module Contents
---------------

.. py:class:: UserManager

   Bases: :py:obj:`django.contrib.auth.base_user.BaseUserManager`\ [\ :py:obj:`loefsys.users.models.User`\ ]


   Custom user manager.

   Custom user model manager where email is the unique identifiers
   for authentication instead of usernames.


   .. py:method:: create_user(email, password, **extra_fields)

      Create and save a user with the given email and password.



   .. py:method:: create_superuser(email, password, **extra_fields)

      Create and save a SuperUser with the given email and password.



