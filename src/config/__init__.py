# src/config/__init__.py

import json
import os

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), 'llm_config.json')
    with open(config_path, 'r') as file:
        config = json.load(file)
    return config
