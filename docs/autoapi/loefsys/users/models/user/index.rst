loefsys.users.models.user
=========================

.. py:module:: loefsys.users.models.user


Classes
-------

.. autoapisummary::

   loefsys.users.models.user.User


Module Contents
---------------

.. py:class:: User(*args, **kwargs)

   Bases: :py:obj:`django.contrib.auth.models.AbstractBaseUser`, :py:obj:`django.contrib.auth.models.PermissionsMixin`


   Make subclasses preserve the alters_data attribute on overridden methods.


   .. py:attribute:: email


   .. py:attribute:: is_staff


   .. py:attribute:: is_active


   .. py:attribute:: USERNAME_FIELD
      :value: 'email'



   .. py:attribute:: REQUIRED_FIELDS
      :value: []



   .. py:attribute:: objects


   .. py:attribute:: membership_set
      :type:  django.db.models.QuerySet[loefsys.users.models.membership.Membership]


   .. py:method:: __str__()

      Return str(self).



