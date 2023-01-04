"""
This script is meant to run all AOC code,
and collect the outputs into the output file.

The code is expected to print outputs to stdout,
and then this script will put them into .txt files
labelled by language.
"""
import subprocess
import os
import time
from io import TextIOWrapper

def run_one(cmd: list[str], cwd: str, err_file: TextIOWrapper):
    """Runs a single AOC directory"""
    lang_name = cwd.capitalize()
    print(f'Running {lang_name} code...')
    start = time.perf_counter()
    output_filename = f'outputs/{cwd}.txt'
    with open(output_filename, 'w', encoding='utf-8') as out_file:
        subprocess.Popen(
            cmd,
            cwd=cwd,
            stdout=out_file,
            stderr=err_file,
        )
    print(f'{lang_name} took {time.perf_counter()-start} seconds\n')


def run_all():
    """Runs all of the AOC code"""

    # Create output directory
    if not os.path.exists('outputs'):
        os.makedirs('outputs')

    # Error file
    err_file = open('outputs/errors.txt', 'w', encoding='utf-8')

    py_cwd = 'python'
    py_cmd = ['python', 'main.py']
    run_one(py_cmd, py_cwd, err_file)

    ts_cwd = 'typescript'
    ts_cmd = ['npm', 'run', 'start']
    run_one(ts_cmd, ts_cwd, err_file)

    rs_cwd = 'rust'
    rs_cmd = ['cargo', 'run', '-r']
    run_one(rs_cmd, rs_cwd, err_file)

    ex_cwd = 'elixir'
    ex_cmd = ['mix', 'run', 'aoc.exs']
    run_one(ex_cmd, ex_cwd, err_file)

    err_file.close()

    print('Check the outputs/ directory for the results!')

if __name__ == '__main__':
    run_all()
