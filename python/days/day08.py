"""Day 8 of AOC 2022: ???"""

# -------------- Public Functions ------------- #

def day08_pt1(filename: str) -> int:
    """Day 8, part 1: ???"""
    with open(filename, 'r', encoding='utf-8') as input_file:
        lines = input_file.read().split('\n')[:-1]

    return 0

def day08_pt2(filename: str) -> int:
    """Day 8, part 2: ???"""
    with open(filename, 'r', encoding='utf-8') as input_file:
        lines = input_file.read().split('\n')[:-1]

    return 0


# ----------------- Constants ----------------- #


# ------------- Private Functions ------------- #


# ------------------- Script ------------------ #

if __name__ == '__main__':
    INPUT_FILENAME = '../inputs/08.txt'
    print(f'Day 8, pt1: {day08_pt1(INPUT_FILENAME)}')
    print(f'Day 8, pt2: {day08_pt2(INPUT_FILENAME)}')
