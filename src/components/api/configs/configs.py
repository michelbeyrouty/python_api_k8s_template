from functools import lru_cache

from components.api.configs.settings import Settings


@lru_cache()
def get_settings() -> Settings:
    return Settings()
