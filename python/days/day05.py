"""Day 5 of AOC 2022: Supply Stacks"""

# -------------- Public Functions ------------- #

def day05_pt1(filename: str) -> str:
    """Day 5, part 1: Crate Mover 9000"""
    init_crates, moves = _split_input(filename)

    supply_stacks = SupplyStacks(init_crates)

    for move in moves:
        supply_stacks.crate_mover_9000(move)

    return supply_stacks.top_crates()

def day05_pt2(filename: str) -> str:
    """Day 5, part 2: Crate Mover 9001"""
    init_crates, moves = _split_input(filename)

    supply_stacks = SupplyStacks(init_crates)

    for move in moves:
        supply_stacks.crate_mover_9001(move)

    return supply_stacks.top_crates()


# ----------------- Classes ----------------- #

class SupplyStacks:
    """The stacks of crates that we are moving around."""
    crates: list[list[str]]

    def __init__(self, rows: list[str]):
        # TODO:
        num_cols = (len(rows[0]) + 1)//4
        self.crates = [[] for _ in range(num_cols)]
        for row in rows:
            self.add_row(row)

    def add_row(self, row: str):
        """Adds a row of crates to the top of the stacks."""
        crate_list = [row[i:i+4][1] for i in range(0, len(row), 4)]
        for i, crate in enumerate(crate_list):
            if crate != ' ':
                self.crates[i].append(crate)

    def crate_mover_9000(self, move: str):
        """Move crates as specified by the Crate Mover 9000 manual."""
        num_crates, from_stack, to_stack = _parse_move(move)
        for _ in range(num_crates):
            self.crates[to_stack].append(self.crates[from_stack].pop())

    def crate_mover_9001(self, move: str):
        """Move crates as specified by the Crate Mover 9001 manual."""
        num_crates, from_stack, to_stack = _parse_move(move)

        self.crates[to_stack] += self.crates[from_stack][-num_crates:]
        self.crates[from_stack] = self.crates[from_stack][:-num_crates]

    def top_crates(self) -> str:
        """Get a string of the set of crates at the top of each stack."""
        return ''.join([col.pop() for col in self.crates])

# ----------------- Constants ----------------- #


# ------------- Private Functions ------------- #

def _split_input(filename: str) -> list[list[str]]:
    with open(filename, 'r', encoding='utf-8') as input_file:
        lines = input_file.read().split('\n\n')

    [init_crates, moves] = list(map(
        lambda line: line.split('\n')[:-1],
        lines,
    ))

    init_crates = list(reversed(init_crates))

    return init_crates, moves

def _parse_move(move_str: str) -> tuple[int, int, int]:
    [num_crates, from_stack, to_stack] = list(map(int, move_str.split(' ')[1::2]))
    return num_crates, from_stack - 1, to_stack - 1


# ------------------- Script ------------------ #

if __name__ == '__main__':
    INPUT_FILENAME = '../inputs/05.txt'
    print(f'Day 5, pt1: {day05_pt1(INPUT_FILENAME)}')
    print(f'Day 5, pt2: {day05_pt2(INPUT_FILENAME)}')
