"""Day 7 of AOC 2022: No Space Left On Device"""

# -------------- Public Functions ------------- #

def day07_pt1(filename: str) -> int:
    """Day 7, part 1: Sum of small directories."""
    with open(filename, 'r', encoding='utf-8') as input_file:
        lines = input_file.read().split('\n')[:-1]

    file_system = FileSystem()
    for line in lines:
        file_system.parse_line(line)

    return sum(file_system.get_small_dirs())

def day07_pt2(filename: str) -> int:
    """Day 7, part 2: Smallest directory to delete."""
    with open(filename, 'r', encoding='utf-8') as input_file:
        lines = input_file.read().split('\n')[:-1]

    file_system = FileSystem()
    for line in lines:
        file_system.parse_line(line)

    return file_system.get_dir_size(file_system.min_dir_to_remove())

# ------------------ Classes ------------------ #

class FileSystem:
    """Class for keeping track of directory traversal."""
    _curr_dir: str
    _directories: dict[str]
    _total_space: int

    def __init__(self, total_space=70_000_000):
        self._curr_dir = '/'
        self._directories = {'/': 0}
        self._total_space = total_space

    def parse_line(self, line: str):
        """Parses a line from the inputfile."""
        match line.split():
            case ['$', 'cd', dir_name]:
                self._change_dir(dir_name)
            case ['$', 'ls']:
                pass
            case ['dir', dir_name]:
                self._add_dir(dir_name)
            case [size, _file_name]:
                self._add_file(int(size))
            case _:
                raise Exception(f'This should not occur...\n\t{line.split()}')

    def get_small_dirs(self, size_limit=100_000) -> list[int]:
        """Get a list of all the small directories."""
        small_dirs = []

        for directory in self._directories.values():
            if directory <= size_limit:
                small_dirs.append(directory)

        return small_dirs

    def get_dir_size(self, dir_name: str) -> int:
        """Get the size of a directory, given its name."""
        return self._directories[dir_name] # Bad error handling

    def min_dir_to_remove(self, space_needed=30_000_000) -> str:
        """Find the smallest directory to remove to get the space needed."""
        space_to_remove = space_needed - self.space_left()

        return min([
                (name, size) for (name, size) in self._directories.items()
                if size >= space_to_remove
            ],
            key=lambda tpl: tpl[1]
        )[0]

    def space_left(self) -> int:
        """Get how much space is left in the file system."""
        return self._total_space - self._directories['/']

    def _change_dir(self, dir_name: str):
        match dir_name:
            case '..':
                if self._curr_dir != '/':
                    self._curr_dir = '/'.join(self._curr_dir.split('/')[:-2]) + '/'
            case '/':
                self._curr_dir = '/'
            case new_dir:
                self._curr_dir += new_dir + '/'

    def _add_dir(self, dir_name: str):
        new_dir = self._curr_dir + dir_name + '/'
        if not new_dir in self._directories:
            self._directories[new_dir] = 0

    def _add_file(self, file_size: int):
        curr = '/'
        for directory in self._curr_dir.split('/')[1:]:
            self._directories[curr] += file_size
            curr += directory + '/'


# ----------------- Constants ----------------- #


# ------------- Private Functions ------------- #


# ------------------- Script ------------------ #

if __name__ == '__main__':
    INPUT_FILENAME = '../inputs/07.txt'
    print(f'Day 7, pt1: {day07_pt1(INPUT_FILENAME)}')
    print(f'Day 7, pt2: {day07_pt2(INPUT_FILENAME)}')
