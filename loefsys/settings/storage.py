from cbs import env

from .base import BaseSettings
from .templates import TemplateSettings


class StorageSettings(TemplateSettings, BaseSettings):
    AWS_STORAGE_BUCKET_NAME = env(None)

    def AWS_S3_CUSTOM_DOMAIN(self):  # noqa N802
        return f"{self.AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

    def STATIC_URL(self):  # noqa N802
        return f"https://{self.AWS_S3_CUSTOM_DOMAIN}/static/"

    def MEDIA_URL(self):  # noqa N802
        return f"https://{self.AWS_S3_CUSTOM_DOMAIN}/media/"

    def STATIC_DIR(self):  # noqa N802
        return self.BASE_DIR / "staticfiles"

    def MEDIA_DIR(self):  # noqa N802
        return self.BASE_DIR / "mediafiles"

    def DJANGO_APPS(self):  # noqa N802
        return super().DJANGO_APPS() + ["django.contrib.staticfiles"]

    def STORAGES(self):  # noqa N802
        return {
            "default": {
                "BACKEND": "storages.backends.s3boto3.S3Boto3Storage"
                if self.AWS_STORAGE_BUCKET_NAME
                else "django.core.files.storage.FileSystemStorage"
            },
            "staticfiles": {
                "BACKEND": "storages.backends.s3boto3.S3StaticStorage"
                if self.AWS_STORAGE_BUCKET_NAME
                else "django.contrib.staticfiles.storage.StaticFilesStorage"
            },
        }

    def templates_context_processors(self):
        return super().templates_context_processors() + [
            "django.template.context_processors.media",
            "django.template.context_processors.static",
        ]
