"""Day 1 of AOC 2022"""

def day02_pt1(filename: str) -> int:
    """Get the total score from following the strategy"""
    with open(filename, 'r', encoding='utf-8') as games_file:
        games = games_file.read()
        return sum(map(_parse_rock_paper_scissors, games.split('\n')[:-1]))

def day02_pt2(filename: str) -> int:
    """Day 2, part 2"""
    print(f'{filename} pt2 to be implemented')
    return 0

def _parse_rock_paper_scissors(game: str) -> int:
    # FIXME: first column is what your opponent plays!!
    player_1, player_2, *_ = map(ord, game.split(' '))

    total_pts = player_2 - 87
    player_2 -= 23
    if player_1 == player_2:
        total_pts += 3
    elif (player_2 - player_1) % 3 == 1:
        total_pts += 6

    return total_pts
