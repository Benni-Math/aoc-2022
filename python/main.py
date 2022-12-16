"""The main file for running all AOC Days"""
# Import helpers
import os

# Import AOC code
from days import day_solutions

# Constants
INPUT_DIR = '../inputs'

def main():
    """Runs all of the AOC days solutions"""
    for day, input_name in enumerate(sorted(os.listdir(INPUT_DIR))):
        input_filename = f'{INPUT_DIR}/{input_name}'
        for part, soln_func in enumerate(day_solutions[day]):
            answer = soln_func(input_filename)

            print(f'Day {day+1}, pt{part+1}: {answer}')

if __name__ == '__main__':
    main()
