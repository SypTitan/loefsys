from .auth import AuthSettings
from .base import BaseSettings
from .templates import TemplateSettings


class AdminSettings(AuthSettings, TemplateSettings, BaseSettings):
    def DJANGO_APPS(self):  # noqa N802
        return super().DJANGO_APPS() + [
            "django.contrib.messages",
            "django.contrib.admin",
        ]

    def MIDDLEWARE(self):  # noqa N802
        return super().MIDDLEWARE() + [
            "django.contrib.messages.middleware.MessageMiddleware"
        ]

    def templates_context_processors(self):
        return super().templates_context_processors() + [
            "django.contrib.messages.context_processors.messages"
        ]
