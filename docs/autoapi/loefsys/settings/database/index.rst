loefsys.settings.database
=========================

.. py:module:: loefsys.settings.database


Attributes
----------

.. autoapisummary::

   loefsys.settings.database.denv


Classes
-------

.. autoapisummary::

   loefsys.settings.database.DatabaseSettings


Module Contents
---------------

.. py:data:: denv

.. py:class:: DatabaseSettings

   Bases: :py:obj:`loefsys.settings.base.BaseSettings`


   Base class for settings configuration.

   The base class configures essential variables, such as the debug mode, which may be
   required by other modules.


   .. py:attribute:: default_database_url


   .. py:attribute:: conn_max_age


   .. py:method:: DATABASES()


