"""Day 6 of AOC 2022: Tuning Trouble"""

# -------------- Public Functions ------------- #

def day06_pt1(filename: str) -> int:
    """Day 6, part 1: Find start-of-packet marker"""
    with open(filename, 'r', encoding='utf-8') as input_file:
        stream = input_file.read()

    return _find_marker(stream, 4)

def day06_pt2(filename: str) -> int:
    """Day 6, part 2: Find start-of-message marker"""
    with open(filename, 'r', encoding='utf-8') as input_file:
        stream = input_file.read()

    return _find_marker(stream, 14)


# ----------------- Constants ----------------- #


# ------------- Private Functions ------------- #

def _is_str_uniq(string: str) -> bool:
    chars = set()
    for char in string:
        if char in chars:
            return False
        else:
            chars.add(char)

    return True

def _find_marker(stream: str, marker_size: int, identifier=_is_str_uniq) -> int:
    sliding_window = (stream[i:i+marker_size] for i in range(len(stream)-marker_size))
    for i, marker in  enumerate(sliding_window):
        if identifier(marker):
            return i + marker_size



# ------------------- Script ------------------ #

if __name__ == '__main__':
    INPUT_FILENAME = '../inputs/06.txt'
    print(f'Day 6, pt1: {day06_pt1(INPUT_FILENAME)}')
    print(f'Day 6, pt2: {day06_pt2(INPUT_FILENAME)}')
