"""Day 17 of AOC 2022: ???"""

# -------------- Public Functions ------------- #

def day17_pt1(filename: str) -> int:
    """Day 17, part 1: ???"""
    with open(filename, 'r', encoding='utf-8') as input_file:
        lines = input_file.read().split('\n')[:-1]

    return 0

def day17_pt2(filename: str) -> int:
    """Day 17, part 2: ???"""
    with open(filename, 'r', encoding='utf-8') as input_file:
        lines = input_file.read().split('\n')[:-1]

    return 0


# ----------------- Constants ----------------- #


# ------------- Private Functions ------------- #


# ------------------- Script ------------------ #

if __name__ == '__main__':
    INPUT_FILENAME = '../inputs/09.txt'
    print(f'Day 17, pt1: {day17_pt1(INPUT_FILENAME)}')
    print(f'Day 17, pt2: {day17_pt2(INPUT_FILENAME)}')
