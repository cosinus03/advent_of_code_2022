
INPUT_FILE = "day1_input.txt"


def most_calories(filename: str) -> int:
    cals = (open(filename, "r")).read().splitlines()

    elf_sum = 0
    max_elf_sum = 0

    for cal in cals:
        if cal != '':
            elf_sum += int(cal)
        else:
            max_elf_sum = max(max_elf_sum, elf_sum)
            elf_sum = 0

    return max_elf_sum

print("Part One: ", most_calories(INPUT_FILE))


def most_calories_top_three(filename: str) -> int:
    cals = (open(filename, "r")).read().splitlines()

    elf_sum_list = []
    elf_sum = 0

    for cal in cals:
        if cal != '':
            elf_sum += int(cal)
        else:
            elf_sum_list.append(elf_sum)
            elf_sum = 0

    return sum(sorted(elf_sum_list)[-3:])

print("Part Two: ", most_calories_top_three(INPUT_FILE))


def most_calories_top_three_On(filename: str) -> int:
    cals = (open(filename, "r")).read().splitlines()

    elf_sum_list = [0, 0, 0]
    elf_sum = 0

    for cal in cals:
        if cal != '':
            elf_sum += int(cal)
        else:
            if elf_sum >= elf_sum_list[0]:
                elf_sum_list[0] = elf_sum
                elf_sum_list.sort()
            elf_sum = 0

    return sum(elf_sum_list)

print("Part Two On: ", most_calories_top_three_On(INPUT_FILE))
