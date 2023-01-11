"""Day 2 of AOC 2022: Rock Paper Scissors"""

# -------------- Public Functions ------------- #

def day02_pt1(filename: str) -> int:
    """Day 2, part 1: Assuming the strategy, what score do you get?"""
    with open(filename, 'r', encoding='utf-8') as games_file:
        games = games_file.read().split('\n')[:-1]

    return sum(map(_score_rps_wrong, games))

def day02_pt2(filename: str) -> int:
    """Day 2, part 2: Given the elf's strategy, what score do you get?"""
    with open(filename, 'r', encoding='utf-8') as games_file:
        games = games_file.read().split('\n')[:-1]

    return sum(map(_score_rps_right, games))


# ----------------- Constants ----------------- #

_wrong_score = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}

_right_score = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
}


# ------------- Private Functions ------------- #

def _score_rps_wrong(game: str) -> int:
    return _wrong_score.get(game, 0)

def _score_rps_right(game: str) -> int:
    return _right_score.get(game, 0)

# ------------------- Script ------------------ #

if __name__ == '__main__':
    INPUT_FILENAME = '../inputs/02.txt'
    print(f'Day 2, pt1: {day02_pt1(INPUT_FILENAME)}')
    print(f'Day 2, pt2: {day02_pt2(INPUT_FILENAME)}')
