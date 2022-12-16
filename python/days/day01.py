"""Day 1 of AOC 2022"""
from .util import parse_int

def day01_part1(filename: str) -> int:
    """Main function"""
    with open(filename, 'r', encoding='utf-8') as inputfile:
        food_list = inputfile.read()

    return max([
        sum(
            map(parse_int, elf.split('\n'))
        ) for elf in food_list.split('\n\n')
    ])

if __name__ == '__main__':
    INPUT_FILENAME = '../../inputs/01.txt'
    print(f'Day 1, pt1: {day01_part1(INPUT_FILENAME)}')
