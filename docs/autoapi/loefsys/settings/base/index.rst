loefsys.settings.base
=====================

.. py:module:: loefsys.settings.base


Attributes
----------

.. autoapisummary::

   loefsys.settings.base.denv


Classes
-------

.. autoapisummary::

   loefsys.settings.base.BaseSettings


Module Contents
---------------

.. py:data:: denv

.. py:class:: BaseSettings

   Bases: :py:obj:`cbs.BaseSettings`


   Base class for settings configuration.

   The base class configures essential variables, such as the debug mode, which may be
   required by other modules.


   .. py:attribute:: BASE_DIR


   .. py:attribute:: DEBUG


   .. py:attribute:: ALLOWED_HOSTS


   .. py:attribute:: ROOT_URLCONF
      :value: 'loefsys.urls'



   .. py:attribute:: WSGI_APPLICATION
      :value: 'loefsys.wsgi.application'



   .. py:method:: SECRET_KEY() -> str


   .. py:method:: INTERNAL_IPS() -> list[str]


   .. py:method:: DJANGO_APPS() -> list[str]


   .. py:method:: THIRD_PARTY_APPS() -> list[str]


   .. py:method:: LOCAL_APPS() -> list[str]


   .. py:method:: INSTALLED_APPS() -> list[str]


   .. py:method:: MIDDLEWARE() -> list[str]


