from loefsys.settings import BaseSettings, TemplateSettings, AuthSettings


class AdminSettings(AuthSettings, TemplateSettings, BaseSettings):

    def DJANGO_APPS(self):
        return super().DJANGO_APPS() + [
            "django.contrib.messages",
            "django.contrib.admin",
        ]

    def MIDDLEWARE(self):
        return super().MIDDLEWARE() + [
            "django.contrib.messages.middleware.MessageMiddleware"
        ]

    def templates_context_processors(self):
        return super().templates_context_processors() + [
            "django.contrib.messages.context_processors.messages"
        ]
