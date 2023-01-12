"""Module for cleaning compiled artifacts and dependencies in AoC directories."""

import subprocess
import sys

from .config import CONFIG

OUTPUT_DIR = CONFIG['output_dir']

def clean_one(cwd: str = None, cmd: list[str] = None):
    """Clean artifacts from an AoC directory."""
    if cwd is None:
        try:
            if sys.argv[1] in CONFIG['clean']:
                cwd = sys.argv[1]
            else:
                msg = f'Cleaning for this language ({sys.argv[1]}) is not implemented!'
                raise NotImplementedError(msg)
        except IndexError as exc:
            raise Exception('Please pass in a language to clean.') from exc

    if cmd is None:
        cmd = CONFIG['compile'][cwd].split()

    print(f'Cleaning up {cwd.capitalize()} artifacts...')
    subprocess.Popen(
        cmd,
        cwd=cwd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT,
    ).wait()
    print('Finished cleaning!\n')

def clean_all():
    """Script which cleans all of the directories."""
    for cwd in CONFIG['languages']:
        if cwd in CONFIG['clean']:
            clean_one(cwd=cwd)
