"""Day 1 of AOC 2022"""

def day01():
    """Main function"""
    with open('../inputs/day01-input.txt', 'r', encoding='utf-8') as inputfile:
        food_list = inputfile.read()

    def parse_int(num: str) -> int:
        try:
            return int(num)
        except ValueError:
            return 0

    return max([
        sum(
            map(parse_int, elf.split('\n'))
        ) for elf in food_list.split('\n\n')
    ])

if __name__ == '__main__':
    answer = day01()
    print(answer)
