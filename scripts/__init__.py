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

OUTPUT_DIR = 'outputs'
INPUT_DIR = 'inputs'

def _run_one(cmd: list[str], cwd: str, err_file: TextIOWrapper):
    """Runs a single AOC directory."""
    lang_name = cwd.capitalize()
    print(f'Running {lang_name} code...')
    start = time.perf_counter()
    output_filename = f'{OUTPUT_DIR}/{cwd}.txt'
    with open(output_filename, 'w', encoding='utf-8') as out_file:
        subprocess.Popen(
            cmd,
            cwd=cwd,
            stdout=out_file,
            stderr=err_file,
        ).wait()
    print(f'{lang_name} took {time.perf_counter()-start:.4g} seconds\n')


def compile_all():
    """Compile the projects that need compiling."""

    # Create output directory
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    if not os.path.exists('typescript/node_modules'):
        subprocess.Popen(
            ['npm', 'install'],
            cwd='typescript',
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
        ).wait()

    my_env = os.environ.copy()
    my_env['MIX_ENV'] = 'release'
    print('Compiling...')
    compile_filename = f'{OUTPUT_DIR}/compile.txt'
    with open(compile_filename, 'w', encoding='utf-8') as out_file:
        rs_c = subprocess.Popen(
            ['cargo', 'build', '-r'],
            cwd='rust',
            # stdout=subprocess.DEVNULL,
            stdout=out_file,
            stderr=subprocess.STDOUT,
        )
        ex_c = subprocess.Popen(
            ['mix', 'escript.build'],
            cwd='elixir',
            # stdout=subprocess.DEVNULL,
            stdout=out_file,
            stderr=subprocess.STDOUT,
            env=my_env,
        )
        ts_c = subprocess.Popen(
            ['npm', 'run', 'build'],
            cwd='typescript',
            # stdout=subprocess.DEVNULL,
            stdout=out_file,
            stderr=subprocess.STDOUT,
        )
        c_c = subprocess.Popen(
            ['make'],
            cwd='c',
            stdout=out_file,
            stderr=subprocess.STDOUT,
        )
        _waiting = [p.wait() for p in (rs_c, ex_c, ts_c, c_c)]
    print('Finished compiling.\n')


def run_all():
    """Runs all of the AOC code."""
    if not os.path.exists(INPUT_DIR):
        raise Exception('Create an input directory.')

    # Create output directory
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Error file
    with  open(f'{OUTPUT_DIR}/errors.txt', 'w', encoding='utf-8') as err_file:

        ex_cwd = 'elixir'
        ex_cmd = ['target/aoc-2022']
        _run_one(ex_cmd, ex_cwd, err_file)

        py_cwd = 'python'
        py_cmd = ['poetry', 'run', 'main']
        _run_one(py_cmd, py_cwd, err_file)

        ts_cwd = 'typescript'
        ts_cmd = ['node', 'target/aoc-2022']
        _run_one(ts_cmd, ts_cwd, err_file)

        rs_cwd = 'rust'
        rs_cmd = ['target/release/aoc-2022']
        _run_one(rs_cmd, rs_cwd, err_file)

        rs_cwd = 'c'
        rs_cmd = ['target/bin/aoc-2022']
        _run_one(rs_cmd, rs_cwd, err_file)

    print('Check the outputs/ directory for the results!')

def clean_all():
    """Script which cleans all of the directories."""
    print('Cleaning up...')
    clean_filename = f'{OUTPUT_DIR}/clean_up.txt'
    with open(clean_filename, 'w', encoding='utf-8') as out_file:
        rs_clean = subprocess.Popen(
            ['cargo', 'clean'],
            cwd='rust',
            # stdout=subprocess.DEVNULL,
            stdout=out_file,
            stderr=subprocess.STDOUT,
        )
        ex_clean = subprocess.Popen(
            ['mix', 'clean', '&&', 'rm', '-f', 'target/aoc-2022'],
            cwd='elixir',
            # stdout=subprocess.DEVNULL,
            stdout=out_file,
            stderr=subprocess.STDOUT,
        )
        ts_clean = subprocess.Popen(
            ['npm', 'run', 'clean'],
            cwd='typescript',
            # stdout=subprocess.DEVNULL,
            stdout=out_file,
            stderr=subprocess.STDOUT,
        )
        c_clean = subprocess.Popen(
            ['make', 'clean'],
            cwd='c',
            stdout=out_file,
            stderr=subprocess.STDOUT,
        )
        _waiting = [p.wait() for p in (rs_clean, ex_clean, ts_clean, c_clean)]
    print('Finished cleaning.\n')

def crc_all():
    """Compile, run, and clean all AoC directories."""
    compile_all()   # Comment this out if everything is already compiled
    run_all()
    # clean_all()     # Comment this out if you don't want it to clean


if __name__ == '__main__':
    crc_all()
