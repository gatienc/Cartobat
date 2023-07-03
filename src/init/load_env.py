import os 
from dotenv import load_dotenv

load_dotenv()
if 'SITE_URL' not in os.environ:
    raise ValueError("Please provide SITE_URL in .env file")
elif 'API_KEY' not in os.environ:
    raise ValueError("Please provide API_KEY in .env file")