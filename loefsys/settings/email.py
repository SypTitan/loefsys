class EmailSettings:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_TIMEOUT = 5

    DEFAULT_FROM_EMAIL = "Loefbijter <noreply@loefbijter.nl>"
    EMAIL_SUBJECT_PREFIX = "[Loefbijter]"

    def SERVER_EMAIL(self):
        return self.DEFAULT_FROM_EMAIL
