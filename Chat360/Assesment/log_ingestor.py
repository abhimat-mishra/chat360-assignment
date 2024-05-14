import logging
import os
import json
from datetime import datetime
import requests

# if the fie doesn't exist create it
if not os.path.exists('logs'):
    os.makedirs('logs')

# loggers for different APIs
def configure_logger(api_name):
    logger = logging.getLogger(api_name)
    handler = logging.FileHandler(f'logs/{api_name}.log')
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger

# API logging
api_loggers = {
    'api1': configure_logger('api1'),
    'api2': configure_logger('api2'),
    'api3': configure_logger('api3'),
    'api4': configure_logger('api4'),
    'api5': configure_logger('api5'),
    'api6': configure_logger('api6'),
}

def log_message(api_name, level, message):
    try:
        logger = api_loggers.get(api_name)
        if not logger:
            raise ValueError(f"No logger configured for API: {api_name}")
        
        # format for the loggging in file
        log_entry = {
            "level": level,
            "log_string": message,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "metadata": {
                "source": f"{api_name}.log"
            }
        }

        logger.info(json.dumps(log_entry))

    except Exception as e:
        print(f"Error logging message for {api_name}: {e}")

# call API and log responses
def call_api(api_name, url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        log_message(api_name, 'info', f'Successfully called {url}')
        log_message(api_name, 'success', f'Response: {response.json()}')
    except requests.exceptions.HTTPError as http_err:
        log_message(api_name, 'error', f'HTTP error occurred: {http_err}')
    except Exception as err:
        log_message(api_name, 'error', f'Other error occurred: {err}')

# calling different api some with fake url 
call_api('api1', 'xddfd.com')
call_api('api2', 'https://api.coindesk.com/v1/bpi/currentprice.json')
call_api('api3', 'https://catfact.ninja/fact')
call_api('api4', 'https://randomuser.me/api/')
call_api('api5', 'https://posts')
# call_api('api6', 'https://reqres.in/api/users?page=2')
call_api('api6', 'https://api.ipify.org?format=json')

