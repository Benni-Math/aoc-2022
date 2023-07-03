"""Collection of scripts for running AoC projects."""
import subprocess
import os
import time
from io import TextIOWrapper
import sys

from .config import CONFIG

OUTPUT_DIR = CONFIG['output_dir']
INPUT_DIR = CONFIG['input_dir']

def run_one(
    cwd: str = None,
    cmd: list[str] = None,
    out_file: TextIOWrapper = None,
    err_file: TextIOWrapper = subprocess.STDOUT,
    is_compiled = False,
):
    """Runs a single AOC directory."""
    if cwd is None:
        try:
            if sys.argv[1] in CONFIG['run']:
                cwd = sys.argv[1]
            else:
                msg = f'This language ({sys.argv[1]}) is not implemented!'
                raise NotImplementedError(msg)
        except IndexError as exc:
            raise Exception('Please pass in a language to run.') from exc

    if cmd is None:
        if os.path.exists(f'{cwd}/target') or is_compiled:
            cmd = CONFIG['run'][cwd]['release'].split()
        else:
            cmd = CONFIG['run'][cwd]['dev'].split()

    lang_name = cwd.capitalize()
    print(f'Running {lang_name} code...')
    start = time.perf_counter()
    if out_file is None:
        subprocess.Popen(
            cmd,
            cwd=cwd,
            stderr=err_file,
        ).wait()
    else:
        subprocess.Popen(
            cmd,
            cwd=cwd,
            stdout=out_file,
            stderr=err_file,
        ).wait()

    print(f'{lang_name} took {time.perf_counter()-start:.4g} seconds\n')

def run_all():
    """Runs all of the AOC code."""
    if not os.path.exists(INPUT_DIR):
        raise Exception('Create an input directory.')

    # Create output directory
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Error file
    with  open(f'{OUTPUT_DIR}/errors.txt', 'w', encoding='utf-8') as err_file:
        for cwd in CONFIG['languages']:
            with open(f'{OUTPUT_DIR}/{cwd}.txt', 'w', encoding='utf-8') as out_file:
                run_one(
                    cwd=cwd,
                    out_file=out_file,
                    err_file=err_file,
                )

    print('Check the outputs/ directory for the results!')
