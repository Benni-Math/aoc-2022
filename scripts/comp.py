"""Module for compiling/installing AoC projects."""

import subprocess
import sys

from .config import CONFIG

OUTPUT_DIR = CONFIG['output_dir']

def compile_one(cwd: str = None, cmd: list[str] = None):
    """Compile the code for a single AoC directory."""
    if cwd is None:
        try:
            if sys.argv[1] in CONFIG['compile']:
                cwd = sys.argv[1]
            else:
                msg = f'Compilation for this language ({sys.argv[1]}) is not implemented!'
                raise NotImplementedError(msg)
        except IndexError as exc:
            raise Exception('Please pass in a language to compile.') from exc

    if cmd is None:
        cmd = CONFIG['compile'][cwd].split()

    print(f'Compiling {cwd.capitalize()}...')
    cmd = CONFIG['compile'][cwd].split()
    subprocess.Popen(
        cmd,
        cwd=cwd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT,
    ).wait()
    print('Finished compiling!\n')

def compile_all():
    """Compile the projects that need compiling."""
    for cwd in CONFIG['languages']:
        if cwd in CONFIG['compile']:
            compile_one(cwd=cwd)
