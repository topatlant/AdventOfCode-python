def get_input():
    with open("inputs/02.txt") as f:
        return f.readlines()


def main():
    puzzle = get_input()
    print("Part 1:", part1(puzzle))
    print("Part 2:", part2(puzzle))


def part1(puzzle):
    score = sum(get_score_part1(line) for line in puzzle)
    return score


def part2(puzzle):
    score = sum(get_score_part2(line) for line in puzzle)
    return score


U_ROCK = "A"
U_PAPER = "B"
U_SCISSORS = "C"
I_ROCK = "X"
I_PAPER = "Y"
I_SCISSORS = "Z"
I_LOSE = "X"
I_DRAW = "Y"
I_WIN = "Z"


def get_score_part1(round_: str):
    u_play, i_play = round_.split()
    return get_score(i_play, u_play)


def get_score_part2(round_: str) -> int:
    u_play, result = round_.split()
    i_play = get_my_shape(u_play, result)
    return get_score(i_play, u_play)


def get_score(i_play, u_play):
    scores_shape = {I_ROCK: 1, I_PAPER: 2, I_SCISSORS: 3}
    scores_outcome = {
        (I_ROCK, U_ROCK): 3,
        (I_PAPER, U_PAPER): 3,
        (I_SCISSORS, U_SCISSORS): 3,
        (I_ROCK, U_PAPER): 0,
        (I_ROCK, U_SCISSORS): 6,
        (I_PAPER, U_ROCK): 6,
        (I_PAPER, U_SCISSORS): 0,
        (I_SCISSORS, U_ROCK): 0,
        (I_SCISSORS, U_PAPER): 6,
    }
    return scores_shape[i_play] + scores_outcome[i_play, u_play]


def get_my_shape(u_play, result):
    strategy = {
        (U_ROCK, I_DRAW): I_ROCK,
        (U_PAPER, I_DRAW): I_PAPER,
        (U_SCISSORS, I_DRAW): I_SCISSORS,
        (U_ROCK, I_WIN): I_PAPER,
        (U_ROCK, I_LOSE): I_SCISSORS,
        (U_PAPER, I_WIN): I_SCISSORS,
        (U_PAPER, I_LOSE): I_ROCK,
        (U_SCISSORS, I_WIN): I_ROCK,
        (U_SCISSORS, I_LOSE): I_PAPER,
    }
    return strategy[u_play, result]


if __name__ == "__main__":
    main()
