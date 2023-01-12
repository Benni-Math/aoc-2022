"""Setup of project configuration."""

import json
import os

CONFIG_DIR = '.config'
OUTPUT_DIR = 'outputs'
INPUT_DIR = 'inputs'

CONFIG = {
    'config_dir': CONFIG_DIR,
    'output_dir': OUTPUT_DIR,
    'input_dir': INPUT_DIR,
}

def load_config():
    """Loads in the config - make sure to run before using the CONFIG!"""
    cmd_types = ['languages', 'compile', 'run', 'clean']
    cmd_files = [f'{CONFIG_DIR}/{name}.json' for name in cmd_types]

    for cmd_typename, cmd_filename in zip(cmd_types, cmd_files):
        with open(cmd_filename, 'r', encoding='utf-8') as cmd_json:
            CONFIG[cmd_typename] = json.load(cmd_json)

if 'languages' not in CONFIG:
    load_config()

# Create output directory
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

if not os.path.exists(INPUT_DIR):
    raise Exception('Please create an `inputs/` directory and put your AoC input files there.')
