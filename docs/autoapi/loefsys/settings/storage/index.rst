loefsys.settings.storage
========================

.. py:module:: loefsys.settings.storage


Classes
-------

.. autoapisummary::

   loefsys.settings.storage.StorageSettings


Module Contents
---------------

.. py:class:: StorageSettings

   Bases: :py:obj:`loefsys.settings.templates.TemplateSettings`, :py:obj:`loefsys.settings.base.BaseSettings`


   Base class for settings configuration.

   The base class configures essential variables, such as the debug mode, which may be
   required by other modules.


   .. py:attribute:: AWS_STORAGE_BUCKET_NAME


   .. py:method:: AWS_S3_CUSTOM_DOMAIN()


   .. py:method:: STATIC_URL()


   .. py:method:: MEDIA_URL()


   .. py:method:: STATIC_DIR()


   .. py:method:: MEDIA_DIR()


   .. py:method:: DJANGO_APPS()


   .. py:method:: STORAGES()


   .. py:method:: templates_context_processors()


