class TemplateSettings:
    def TEMPLATES(self):  # noqa N802
        return [
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "APP_DIRS": True,
                "OPTIONS": {"context_processors": self.templates_context_processors()},
            }
        ]

    def templates_context_processors(self):
        return [
            "django.template.context_processors.debug",
            "django.template.context_processors.request",
        ]
