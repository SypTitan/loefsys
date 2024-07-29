loefsys.settings.security
=========================

.. py:module:: loefsys.settings.security


Classes
-------

.. autoapisummary::

   loefsys.settings.security.SecuritySettings


Module Contents
---------------

.. py:class:: SecuritySettings

   Bases: :py:obj:`loefsys.settings.auth.AuthSettings`, :py:obj:`loefsys.settings.base.BaseSettings`


   Base class for settings configuration.

   The base class configures essential variables, such as the debug mode, which may be
   required by other modules.


   .. py:attribute:: SESSION_COOKIE_HTTPONLY
      :value: True



   .. py:attribute:: SESSION_COOKIE_SECURE
      :value: True



   .. py:attribute:: CSRF_COOKIE_HTTPONLY
      :value: True



   .. py:attribute:: CSRF_COOKIE_SECURE
      :value: True



   .. py:attribute:: SECURE_HSTS_SECONDS
      :value: 60



   .. py:attribute:: SECURE_HSTS_INCLUDE_SUBDOMAINS
      :value: True



   .. py:attribute:: SECURE_HSTS_PRELOAD
      :value: True



   .. py:attribute:: SECURE_CONTENT_TYPE_NOSNIFF
      :value: True



   .. py:method:: MIDDLEWARE()


