
from pydantic import BaseSettings


class Settings(BaseSettings):

    """
    In dev, value are set in the local_env/api.cfg file (through docker-compose)
    For production, they should be set through the pipeline
    """

    APPLICATION_NAME: str = 'python_api_k8s_template'
    API_VERSION: str = '1.0.0'
    ENVIRONMENT: str = 'dev'
