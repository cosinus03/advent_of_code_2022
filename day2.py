
INPUT_FILE = "day2_input.txt"

CHOICE_TO_SCORE_MAPPING = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3,
}

KEY_WINS_OVER_VALUE = {
    1: 3,
    2: 1,
    3: 2,
}

WIN_POINTS = 6
DRAW_POINTS = 3


def calculate_my_score(filename: str) -> int:
    rounds = [round.split(" ") for round in open(filename, "r").read().splitlines()]

    my_score = 0

    for round in rounds:
        my_score += CHOICE_TO_SCORE_MAPPING[round[1]]

        if CHOICE_TO_SCORE_MAPPING[round[0]] == CHOICE_TO_SCORE_MAPPING[round[1]]:
            my_score += DRAW_POINTS
        elif CHOICE_TO_SCORE_MAPPING[round[0]] == KEY_WINS_OVER_VALUE[CHOICE_TO_SCORE_MAPPING[round[1]]]:
            my_score += WIN_POINTS

    return my_score

print("Part One:", calculate_my_score(INPUT_FILE))


CHOICE_TO_SCORE_MAPPING_2 = {
    'A': 1,
    'B': 2,
    'C': 3,
}

RESULT_SCORING = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}

VALUE_WINS_OVER_KEY = {v: k for k, v in KEY_WINS_OVER_VALUE.items()}


def calculate_my_score_2(filename: str) -> int:
    rounds = [round.split(" ") for round in open(filename, "r").read().splitlines()]

    my_score = 0

    for round in rounds:
        my_score += RESULT_SCORING[round[1]]

        if round[1] == 'Y':
            my_score += CHOICE_TO_SCORE_MAPPING_2[round[0]]
        elif round[1] == 'Z':
            my_score += VALUE_WINS_OVER_KEY[CHOICE_TO_SCORE_MAPPING[round[0]]]
        else:
            my_score += KEY_WINS_OVER_VALUE[CHOICE_TO_SCORE_MAPPING[round[0]]]

    return my_score

print("Part Two:", calculate_my_score_2(INPUT_FILE))
