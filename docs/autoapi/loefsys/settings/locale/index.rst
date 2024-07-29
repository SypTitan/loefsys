loefsys.settings.locale
=======================

.. py:module:: loefsys.settings.locale


Attributes
----------

.. autoapisummary::

   loefsys.settings.locale.denv


Classes
-------

.. autoapisummary::

   loefsys.settings.locale.LocaleSettings


Module Contents
---------------

.. py:data:: denv

.. py:class:: LocaleSettings

   Bases: :py:obj:`loefsys.settings.auth.AuthSettings`, :py:obj:`loefsys.settings.templates.TemplateSettings`, :py:obj:`loefsys.settings.base.BaseSettings`


   Base class for settings configuration.

   The base class configures essential variables, such as the debug mode, which may be
   required by other modules.


   .. py:attribute:: TIME_ZONE


   .. py:attribute:: LANGUAGE_CODE
      :value: 'en-us'



   .. py:attribute:: USE_I18N
      :value: True



   .. py:attribute:: USE_TZ
      :value: True



   .. py:method:: LOCALE_DIR()


   .. py:method:: LOCALE_PATHS()


   .. py:method:: MIDDLEWARE()


   .. py:method:: templates_context_processors()


