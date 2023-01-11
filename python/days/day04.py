"""Day 4 of AOC 2022: Camp Cleanup"""
from dataclasses import dataclass

# -------------- Public Functions ------------- #

def day04_pt1(filename: str) -> int:
    """Day 4 part 1: Do cleanup zones contain each other?"""
    with open(filename, 'r', encoding='utf-8') as input_file:
        zones = input_file.read().split('\n')[:-1]

    ranges = map(
        lambda zone:
            list(map(Range.from_str, zone.split(','))),
        zones,
    )

    containments = map(
        lambda rngs:
            1 if rngs[0].containment(rngs[1]) else 0,
        ranges,
    )

    return sum(list(containments))

def day04_pt2(filename: str) -> int:
    """Day 4, part 2:  Do cleanup zones overlap each other?"""
    with open(filename, 'r', encoding='utf-8') as input_file:
        zones = input_file.read().split('\n')[:-1]

    ranges = map(
        lambda zone:
            list(map(Range.from_str, zone.split(','))),
        zones,
    )

    overlaps = map(
        lambda rngs:
            1 if rngs[0].overlap(rngs[1]) else 0,
        ranges,
    )

    return sum(overlaps)

# ------------------ Classes ------------------ #

@dataclass
class Range:
    """Class describing an inclusive range from low to high"""
    low: int
    high: int

    @staticmethod
    def from_str(range_str: str) -> 'Range':
        """Parse a string into a Range. Must be of the for 'int-int'."""
        [low, high] = range_str.split('-')
        return Range(int(low), int(high))

    def containment(self, other: 'Range') -> bool:
        """Checks whether either Range contains the other."""
        contains_other = self.low <= other.low and other.high <= self.high
        other_contains = other.low <= self.low and self.high <= other.high
        return contains_other or other_contains

    def overlap(self, other: 'Range') -> bool:
        """Checks whether two ranges overlap"""
        high_low = self.low <= other.low and other.low <= self.high
        low_high = other.low <= self.low and self.low <= other.high
        return high_low or low_high


# ------------------- Script ------------------ #

if __name__ == '__main__':
    INPUT_FILENAME = '../inputs/04.txt'
    print(f'Day 4, pt1: {day04_pt1(INPUT_FILENAME)}')
    print(f'Day 4, pt2: {day04_pt2(INPUT_FILENAME)}')
