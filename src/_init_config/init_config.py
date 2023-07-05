from .load_env import load_env
from .logger_config import logger_config

def init_config():
    load_env()
    logger_config()