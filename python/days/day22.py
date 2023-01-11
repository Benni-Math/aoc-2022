"""Day 22 of AOC 2022: ???"""

# -------------- Public Functions ------------- #

def day22_pt1(filename: str) -> int:
    """Day 22, part 1: ???"""
    with open(filename, 'r', encoding='utf-8') as input_file:
        lines = input_file.read().split('\n')[:-1]

    return 0

def day22_pt2(filename: str) -> int:
    """Day 22, part 2: ???"""
    with open(filename, 'r', encoding='utf-8') as input_file:
        lines = input_file.read().split('\n')[:-1]

    return 0


# ----------------- Constants ----------------- #


# ------------- Private Functions ------------- #


# ------------------- Script ------------------ #

if __name__ == '__main__':
    INPUT_FILENAME = '../inputs/09.txt'
    print(f'Day 22, pt1: {day22_pt1(INPUT_FILENAME)}')
    print(f'Day 22, pt2: {day22_pt2(INPUT_FILENAME)}')
