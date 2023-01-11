"""All solutions for the AOC days"""
# Import helpers
import os

# Import days
from .day01 import *
from .day02 import *
from .day03 import *
from .day04 import *
from .day05 import *
from .day06 import *
from .day07 import *
from .day08 import *
from .day09 import *
from .day10 import *
from .day11 import *
from .day12 import *
from .day13 import *
from .day14 import *
from .day15 import *
from .day16 import *
from .day17 import *
from .day18 import *
from .day19 import *
from .day20 import *
from .day21 import *
from .day22 import *
from .day23 import *
from .day24 import *
from .day25 import *


day_solutions = [
    [day01_pt1, day01_pt2],
    [day02_pt1, day02_pt2],
    [day03_pt1, day03_pt2],
    [day04_pt1, day04_pt2],
    [day05_pt1, day05_pt2],
    [day06_pt1, day06_pt2],
    [day07_pt1, day07_pt2],
    [day08_pt1, day08_pt2],
    [day09_pt1, day09_pt2],
    [day10_pt1, day10_pt2],
    [day11_pt1, day11_pt2],
    [day12_pt1, day12_pt2],
    [day13_pt1, day13_pt2],
    [day14_pt1, day14_pt2],
    [day15_pt1, day15_pt2],
    [day16_pt1, day16_pt2],
    [day17_pt1, day17_pt2],
    [day18_pt1, day18_pt2],
    [day19_pt1, day19_pt2],
    [day20_pt1, day20_pt2],
    [day21_pt1, day21_pt2],
    [day22_pt1, day22_pt2],
    [day23_pt1, day23_pt2],
    [day24_pt1, day24_pt2],
    [day25_pt1, day25_pt2],
]


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
