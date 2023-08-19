import pandas as pd


def read_strategy_data():
    with open('resources/rock_paper_scissors.txt') as strategy:
        return [line.strip() for line in strategy.readlines()]


def outcome_scores_strategy_1():
    games = read_strategy_data()
    score = 0
    score += 6 * (games.count('A Y') + games.count('B Z') + games.count('C X'))
    score += 3 * (games.count('A X') + games.count('B Y') + games.count('C Z'))
    return score


def play_scores_strategy_1():
    games = read_strategy_data()
    moves = [game[2] for game in games]
    score = 0
    score += moves.count('X')
    score += 2 * moves.count('Y')
    score += 3 * moves.count('Z')
    return score


def outcome_scores_strategy_2():
    games = read_strategy_data()
    moves = [game[2] for game in games]
    score = 0
    score += 3 * moves.count('Y')
    score += 6 * moves.count('Z')
    return score


def play_scores_strategy_2():
    games = read_strategy_data()
    score = 0
    score += (games.count('A Y') + games.count('B X') + games.count('C Z'))
    score += 2 * (games.count('A Z') + games.count('B Y') + games.count('C X'))
    score += 3 * (games.count('A X') + games.count('B Z') + games.count('C Y'))
    return score


def total_score():
    return outcome_scores_strategy_2() + play_scores_strategy_2()


if __name__ == '__main__':
    print(total_score())
