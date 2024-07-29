loefsys.settings.admin
======================

.. py:module:: loefsys.settings.admin


Classes
-------

.. autoapisummary::

   loefsys.settings.admin.AdminSettings


Module Contents
---------------

.. py:class:: AdminSettings

   Bases: :py:obj:`loefsys.settings.auth.AuthSettings`, :py:obj:`loefsys.settings.templates.TemplateSettings`, :py:obj:`loefsys.settings.base.BaseSettings`


   Base class for settings configuration.

   The base class configures essential variables, such as the debug mode, which may be
   required by other modules.


   .. py:method:: DJANGO_APPS()


   .. py:method:: MIDDLEWARE()


   .. py:method:: templates_context_processors()


