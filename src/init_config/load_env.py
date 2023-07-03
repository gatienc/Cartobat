import os 
from dotenv import load_dotenv
def load_env():
    """
    Load the environment variables from the .env file.

    Raises:
        ValueError: If the SITE_URL or API_KEY variables are not defined.
    """
    load_dotenv()
    if 'SITE_URL' not in os.environ:
        raise ValueError("Please provide SITE_URL in .env file")
    elif 'API_KEY' not in os.environ:
        raise ValueError("Please provide API_KEY in .env file")
    elif 'TIMEZONE' not in os.environ:
        raise ValueError("Please provide TIMEZONE in .env file, default is 'Europe/Paris'")
