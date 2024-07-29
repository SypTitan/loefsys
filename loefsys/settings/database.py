import dj_database_url
from cbs import env

from .base import BaseSettings

denv = env["DJANGO_"]


class DatabaseSettings(BaseSettings):
    default_database_url = denv("sqlite://:memory:", key="DATABASE_URL")
    conn_max_age = denv.int(60, key="DATABASE_CONN_MAX_AGE")

    def DATABASES(self):  # noqa N802
        return {
            "default": dj_database_url.parse(
                self.default_database_url, conn_max_age=self.conn_max_age
            )
        }
