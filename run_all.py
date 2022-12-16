"""
This script is meant to run all AOC code,
and collect the outputs into the output file.

The code is expected to print outputs to stdout,
and then this script will put them into .txt files
labelled by language.
"""
import subprocess
import os

def run_all():
    """Runs all of the AOC code"""

    # Create output directory
    if not os.path.exists('outputs'):
        os.makedirs('outputs')

    # Error file
    err_file = open('outputs/errors.txt', 'w', encoding='utf-8')

    py_cwd = 'python'
    py_cmd = ['python', 'main.py']
    with open('outputs/python.txt', 'w', encoding='utf-8') as out_file:
        subprocess.Popen(
            py_cmd,
            cwd=py_cwd,
            stdout=out_file,
            stderr=err_file,
        )

    ts_cwd = 'typescript'
    ts_cmd = ['npm', 'run', 'start']
    with open('outputs/typescript.txt', 'w', encoding='utf-8') as out_file:
        subprocess.Popen(
            ts_cmd,
            cwd=ts_cwd,
            stdout=out_file,
            stderr=err_file,
        )

    rs_cwd = 'rust'
    rs_cmd = ['cargo', 'run', '-r']
    with open('outputs/rust.txt', 'w', encoding='utf-8') as out_file:
        subprocess.Popen(
            rs_cmd,
            cwd=rs_cwd,
            stdout=out_file,
            stderr=err_file,
        )

    err_file.close()

if __name__ == '__main__':
    run_all()

