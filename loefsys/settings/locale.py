from cbs import env

from .auth import AuthSettings
from .base import BaseSettings
from .templates import TemplateSettings

denv = env["DJANGO_"]


class LocaleSettings(AuthSettings, TemplateSettings, BaseSettings):
    TIME_ZONE = denv("Europe/Amsterdam")
    LANGUAGE_CODE = "en-us"
    USE_I18N = True
    USE_TZ = True

    def LOCALE_DIR(self):  # noqa N802
        return self.BASE_DIR / "locale"

    def LOCALE_PATHS(self):  # noqa N802
        return [self.LOCALE_DIR]

    def MIDDLEWARE(self):  # noqa N802
        return super().MIDDLEWARE() + ["django.middleware.locale.LocaleMiddleware"]

    def templates_context_processors(self):
        return super().templates_context_processors() + [
            "django.template.context_processors.i18n",
            "django.template.context_processors.tz",
        ]
