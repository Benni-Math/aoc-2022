"""Day 1 of AOC 2022: Calorie Counting"""

from util import parse_int

# ----------- Public Functions ----------- #

def day01_pt1(filename: str) -> int:
    """Get the highest calorie count"""
    with open(filename, 'r', encoding='utf-8') as inputfile:
        food_list = inputfile.read()

    return max([
        sum(
            map(parse_int, elf.split('\n'))
        ) for elf in food_list.split('\n\n')
    ])

def day01_pt2(filename: str) -> int:
    """Get the sum of the top 3 highest calorie counts"""
    with open(filename, 'r', encoding='utf-8') as inputfile:
        food_list = inputfile.read()

    return sum(
        sorted(
            [sum(map(parse_int, elf.split('\n')))
                for elf in food_list.split('\n\n')]
        )[-3:]
    )


if __name__ == '__main__':
    INPUT_FILENAME = '../inputs/01.txt'
    print(f'Day 1, pt1: {day01_pt1(INPUT_FILENAME)}')
    print(f'Day 1, pt2: {day01_pt2(INPUT_FILENAME)}')
