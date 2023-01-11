"""The main file for running all AOC Days"""
# Import helpers
import os

# Import AOC code
from days import day_solutions

# Constants
INPUT_DIR = '../inputs'

def main():
    """Runs all of the AOC days solutions"""
    input_files = sorted(os.listdir(INPUT_DIR))
    for day, (file_name, parts) in enumerate(zip(input_files, day_solutions)):
        input_filename = f'{INPUT_DIR}/{file_name}'
        print(f'Day {day+1}:')
        for part, soln_func in enumerate(parts):
            answer = soln_func(input_filename)

            print(f'  Part {part+1}: {answer}')
        print()

if __name__ == '__main__':
    main()
