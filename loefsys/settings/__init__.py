"""The settings for Django are defined here.

Before the settings are loaded, a file named ``.env`` located in the root of the project
is loaded to populate the environment variables.
"""

from dotenv import load_dotenv

# fmt: off
# isort: off
from loefsys.settings.templates import TemplateSettings
# from loefsys.settings.email import EmailSettings
from loefsys.settings.base import BaseSettings
from loefsys.settings.auth import AuthSettings
# from loefsys.settings.security import SecuritySettings
from loefsys.settings.admin import AdminSettings
from loefsys.settings.database import DatabaseSettings
# from loefsys.settings.locale import LocaleSettings
# from loefsys.settings.logging import LoggingSettings
# from loefsys.settings.storage import StorageSettings
# isort: on
# fmt: on


load_dotenv()


# In principle all individual settings modules work without errors. However, settings
# were directly copied from the old configuration and it may not be correct. That is
# why currently a number of modules are disabled. They can be enabled once we get to
# the part of the app that requires the specific module and we need to set up the
# configuration correctly.
class Settings(
    DatabaseSettings,
    # StorageSettings,
    # LocaleSettings,
    AdminSettings,
    # SecuritySettings,
    AuthSettings,
    # EmailSettings,
    # LoggingSettings,
    TemplateSettings,
    BaseSettings,
):
    """Composite settings class containing the complete configuration.

    This class inherits the settings classes with specific configurations. In principle,
    all individual configuration classes work without errors. However, parts of the
    configuration were directly copied from the old configuration, and thus it is not
    tested whether this works correctly. Some configurations may be disabled because of
    that reason. They can be enabled once that part of the site requires configuration,
    so that we can properly set up that configuration.
    """


__getattr__, __dir__ = Settings.use()
