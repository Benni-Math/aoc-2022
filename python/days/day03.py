"""Day 3 of AOC 2022: Rucksack Reorganization"""

# -------------- Public Functions ------------- #

def day03_pt1(filename: str) -> int:
    """Day 3, part 1: Check for shared items in rucksack pairs."""
    with open(filename, 'r', encoding='utf-8') as input_file:
        rucksacks = input_file.read().split('\n')[:-1]

    shared_items = map(_rucksack_overlap, rucksacks)
    priorities = map(_get_priority, shared_items)

    return sum(priorities)

def day03_pt2(filename: str) -> int:
    """Day 3, part 2: Check group-of-three rucksack overlap"""
    with open(filename, 'r', encoding='utf-8') as input_file:
        rucksacks = input_file.read().split('\n')[:-1]

    num_groups = len(rucksacks)//3
    groups = [[rucksacks[3*i+j] for j in range(3)] for i in range(num_groups)]

    shared_items = map(_group_overlap, groups)
    priorities = map(_get_priority, shared_items)

    return sum(priorities)


# ----------------- Constants ----------------- #


# ------------- Private Functions ------------- #

def _rucksack_overlap(rucksack: str) -> str:
    mid = len(rucksack)//2
    [rucksack_1, rucksack_2] = rucksack[:mid], rucksack[mid:]
    # Inefficient but 'Pythonic'
    for char in rucksack_1:
        if char in rucksack_2:
            return char

    raise Exception('This should not happen...\nCheck ../inputs/02.txt')

def _group_overlap(group: list[str]) -> str:
    [elf1, elf2, elf3] = group

    for char in elf1:
        if char in elf2 and char in elf3:
            return char

    raise Exception('This should not happen...\nCheck ../inputs/02.txt')


def _get_priority(char: str) -> int:
    try:
        ascii_val = ord(char)
        if ascii_val in range(97, 123):
            return ascii_val - 96
        elif ascii_val in range(65, 91):
            return ascii_val - 38
        else:
            return 0
    except TypeError as exc:
        raise Exception('This should not happen...\nCheck ../inputs/02.txt') from exc

# ------------------- Script ------------------ #

if __name__ == '__main__':
    INPUT_FILENAME = '../inputs/03.txt'
    print(f'Day 3, pt1: {day03_pt1(INPUT_FILENAME)}')
    print(f'Day 3, pt2: {day03_pt2(INPUT_FILENAME)}')
