loefsys.settings.auth
=====================

.. py:module:: loefsys.settings.auth


Classes
-------

.. autoapisummary::

   loefsys.settings.auth.AuthSettings


Module Contents
---------------

.. py:class:: AuthSettings

   Bases: :py:obj:`loefsys.settings.templates.TemplateSettings`, :py:obj:`loefsys.settings.base.BaseSettings`


   Base class for settings configuration.

   The base class configures essential variables, such as the debug mode, which may be
   required by other modules.


   .. py:attribute:: AUTH_USER_MODEL
      :value: 'users.User'



   .. py:attribute:: PASSWORD_HASHERS
      :value: ['django.contrib.auth.hashers.Argon2PasswordHasher',...



   .. py:attribute:: AUTH_PASSWORD_VALIDATORS


   .. py:method:: DJANGO_APPS()


   .. py:method:: THIRD_PARTY_APPS()


   .. py:method:: LOCAL_APPS()


   .. py:method:: MIDDLEWARE()


   .. py:method:: templates_context_processors()


