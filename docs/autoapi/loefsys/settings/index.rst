loefsys.settings
================

.. py:module:: loefsys.settings

.. autoapi-nested-parse::

   The settings for Django are defined here.

   Before the settings are loaded, a file named ``.env`` located in the root of the project
   is loaded to populate the environment variables.



Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/loefsys/settings/admin/index
   /autoapi/loefsys/settings/auth/index
   /autoapi/loefsys/settings/base/index
   /autoapi/loefsys/settings/database/index
   /autoapi/loefsys/settings/email/index
   /autoapi/loefsys/settings/locale/index
   /autoapi/loefsys/settings/logging/index
   /autoapi/loefsys/settings/security/index
   /autoapi/loefsys/settings/storage/index
   /autoapi/loefsys/settings/templates/index


Classes
-------

.. autoapisummary::

   loefsys.settings.TemplateSettings
   loefsys.settings.BaseSettings
   loefsys.settings.AuthSettings
   loefsys.settings.AdminSettings
   loefsys.settings.DatabaseSettings
   loefsys.settings.Settings


Package Contents
----------------

.. py:class:: TemplateSettings

   .. py:method:: TEMPLATES()


   .. py:method:: templates_context_processors()


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


.. py:class:: AdminSettings

   Bases: :py:obj:`loefsys.settings.auth.AuthSettings`, :py:obj:`loefsys.settings.templates.TemplateSettings`, :py:obj:`loefsys.settings.base.BaseSettings`


   Base class for settings configuration.

   The base class configures essential variables, such as the debug mode, which may be
   required by other modules.


   .. py:method:: DJANGO_APPS()


   .. py:method:: MIDDLEWARE()


   .. py:method:: templates_context_processors()


.. py:class:: DatabaseSettings

   Bases: :py:obj:`loefsys.settings.base.BaseSettings`


   Base class for settings configuration.

   The base class configures essential variables, such as the debug mode, which may be
   required by other modules.


   .. py:attribute:: default_database_url


   .. py:attribute:: conn_max_age


   .. py:method:: DATABASES()


.. py:class:: Settings

   Bases: :py:obj:`database.DatabaseSettings`, :py:obj:`admin.AdminSettings`, :py:obj:`auth.AuthSettings`, :py:obj:`templates.TemplateSettings`, :py:obj:`base.BaseSettings`


   Composite settings class containing the complete configuration.

   This class inherits the settings classes with specific configurations. In principle,
   all individual configuration classes work without errors. However, parts of the
   configuration were directly copied from the old configuration, and thus it is not
   tested whether this works correctly. Some configurations may be disabled because of
   that reason. They can be enabled once that part of the site requires configuration,
   so that we can properly set up that configuration.


