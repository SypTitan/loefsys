from loefsys.settings.base import BaseSettings
from loefsys.settings.email import EmailSettings
from loefsys.settings.templates import TemplateSettings
from loefsys.settings.auth import AuthSettings
from loefsys.settings.security import SecuritySettings
from loefsys.settings.admin import AdminSettings
from loefsys.settings.database import DatabaseSettings
from loefsys.settings.locale import LocaleSettings
from loefsys.settings.logging import LoggingSettings
from loefsys.settings.storage import StorageSettings

from dotenv import load_dotenv

load_dotenv()

# In principle all individual settings modules work without errors. However, settings
# were directly copied from the old configuration and it may not be correct. That is
# why currently a number of modules are disabled. They can be enabled once we get to
# the part of the app that requires the specific module and we need to set up the
# configuration correctly.
class Settings(
    DatabaseSettings,
    #StorageSettings,
    #LocaleSettings,
    #AdminSettings,
    #SecuritySettings,
    #AuthSettings,
    #EmailSettings,
    #LoggingSettings,
    TemplateSettings,
    BaseSettings
):
    pass


__getattr__, __dir__ = Settings.use()
