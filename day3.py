INPUT_FILE = "day3_input.txt"

def common_character(string_: str) -> str:
    str_len = len(string_)

    first_half = set(string_[:str_len//2])
    second_half = set(string_[str_len//2:])

    return first_half.intersection(second_half).pop()


def get_item_priority(char: str) -> int:
    ascii_ord = ord(char)

    if char.islower():
        return ascii_ord - 96
    else:
        return ascii_ord - 38


def get_rucksacks(filename: str) -> "list[str]":
    return (open(filename, "r")).read().splitlines()


def common_items_sum(filename: str) -> int:
    return sum(get_item_priority(common_character(rucksack)) for rucksack in get_rucksacks(filename))


print("Part One:", common_items_sum(INPUT_FILE))


def get_badge(string1: str, string2: str, string3: str) -> str:
    return set(string1).intersection(set(string2)).intersection(set(string3)).pop()


def badge_sum(filename: str) -> int:
    rucksacks = get_rucksacks(filename)
    return sum(get_item_priority(get_badge(rucksacks[i], rucksacks[i+1], rucksacks[i+2])) for i in range(0, len(rucksacks), 3))


print("Part Two:", badge_sum(INPUT_FILE))