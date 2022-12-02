import string

f = open('input')
input_lines = f.readlines()

ROCK = "ROCK"
PAPER = "PAPER"
SCISSORS = "SCISSORS"

LOSE = "LOSE"
DRAW = "DRAW"
WIN = "WIN"

opponent_code = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS
}

me_code = {
    "X": LOSE,
    "Y": DRAW,
    "Z": WIN
}

win = {
    ROCK: PAPER,
    PAPER: SCISSORS,
    SCISSORS: ROCK
}

lose = {
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
    elif win[opponent] == me:
        score += 6
    else:
        score += 0

    score += shape_points[me]
    return score

def get_my_play(opponent_play, me_strategy):
    if me_strategy == DRAW:
        return opponent_play
    elif me_strategy == WIN:
        return win[opponent_play]
    else:
        return lose[opponent_play]

my_total = 0
for line in input_lines:
    code = line.strip('\n').split(' ')
    opponent_play = opponent_code[code[0]]
    me_strategy = me_code[code[1]]
    me_play = get_my_play(opponent_play, me_strategy)
    score = get_score(me_play, opponent_play)
    my_total += score
    print(opponent_play, me_play, me_strategy, score, my_total)