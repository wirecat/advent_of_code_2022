import string

f = open('test_input')
input_lines = f.readlines()

ROCK = "ROCK"
PAPER = "PAPER"
SCISSORS = "SCISSORS"

opponent_code = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS
}

me_code = {
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS
}

strategy = {
    ROCK: PAPER,
    PAPER: ROCK,
    SCISSORS: SCISSORS
}

victory = {
    ROCK: SCISSORS,
    PAPER: ROCK,
    SCISSORS: PAPER
}

shape_points = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3
}

def get_score(me, opponent):
    score = 0
    if me == opponent:
        score += 3
    elif victory[me] == opponent:
        score += 6
    else:
        score += 0

    score += shape_points[me]
    return score

my_total = 0
for line in input_lines:
    code = line.strip('\n').split(' ')
    opponent = opponent_code[code[0]]
    me = me_code[code[1]]
    score = get_score(me, opponent)
    my_total += score
    print(opponent, me, score, my_total)