import logging
import os
DEBUG = os.getenv('DEBUG', 'False').lower() in {'true', '1', 'yes'}
logger = logging.getLogger('cartobat')
logger.setLevel(log_lvl := logging.DEBUG if DEBUG else logging.INFO)
# Creation of a flow manager for the console
console_handler = logging.StreamHandler()

# Configuration of the level of journalization of the flow manager

console_handler.setLevel(logging.DEBUG)

# Configuration of the format of Journalization Messages
formatter = logging.Formatter('%(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Addition of the flow manager to the logger
logger.addHandler(console_handler)

# Example of journalization messages

logger.debug('Ceci est un message de débogage')
logger.info('Ceci est un message informatif')
logger.warning('Ceci est un avertissement')
logger.error('Ceci est une erreur')
logger.critical('Ceci est une erreur critique')