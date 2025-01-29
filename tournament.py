import random as rnd
from tabulate import tabulate


def main():
    strategies = [
        all_cooperate, 
        all_defect, 
        random, 
        tit_for_tat,
        grim_trigger,
        period_punishment_2,
        period_punishment_5,
        period_punishment_10,
    ] # add your strategy function here

    conduct_tournament(strategies)


def all_cooperate(your_history: list[str], opponent_history: list[str]) -> str:
    return 'C'


def all_defect(your_history: list[str], opponent_history: list[str]) -> str:
    return 'D'


def random(your_history: list[str], opponent_history: list[str]) -> str:
    if rnd.randint(0, 1) == 0:
        return 'C'
    return 'D'


def tit_for_tat(your_history: list[str], opponent_history: list[str]) -> str:
    if not opponent_history:
        return 'C'
    return opponent_history[-1]


def grim_trigger(your_history: list[str], opponent_history: list[str]) -> str:
    return 'C' if all(move == 'C' for move in opponent_history) else 'D'


def period_punishment_k(your_history: list[str], opponent_history: list[str], k) -> str:
    return 'C' if all(move == 'C' for move in opponent_history[-k:]) else 'D'


def period_punishment_2(your_history: list[str], opponent_history: list[str]) -> str:
    return period_punishment_k(your_history, opponent_history, k=2)


def period_punishment_5(your_history: list[str], opponent_history: list[str]) -> str:
    return period_punishment_k(your_history, opponent_history, k=5)


def period_punishment_10(your_history: list[str], opponent_history: list[str]) -> str:
    return period_punishment_k(your_history, opponent_history, k=10)


NUM_ROUNDS = 100
GAME_VERSION = 0 # 0 if R0, 1 if R1

R0 = {
    ('C', 'C'): (3, 3),
    ('C', 'D'): (0, 5),
    ('D', 'C'): (5, 0),
    ('D', 'D'): (1, 1),
}

R1 = {
    ('C', 'C'): (3, 3),
    ('C', 'D'): (0, 8),
    ('D', 'C'): (8, 0),
    ('D', 'D'): (1, 1),
}


def calculate_payoffs(x: str, y: str, game_version=0) -> (int, int):
    assert x in ['C', 'D']
    assert y in ['C', 'D']
    if game_version == 0:
        return R0[(x, y)]
    else:
        return R1[(x, y)]


def run_battle(strategy1, strategy2):
    history1 = []
    history2 = []
    payoffs = [0, 0]
    for round in range(NUM_ROUNDS):
        x = strategy1(history1, history2)
        y = strategy2(history2, history1)
        tmp_payoffs = calculate_payoffs(x, y, game_version=GAME_VERSION)
        history1.append(x)
        history2.append(y)
        payoffs[0] += tmp_payoffs[0]
        payoffs[1] += tmp_payoffs[1]
    return payoffs


def conduct_tournament(strategies):
    N = len(strategies)
    results = [[None] * N for _ in range(N)]
    for i in range(N):
        for j in range(i, N):
            payoffs = run_battle(strategies[i], strategies[j])
            results[i][j] = payoffs.copy()
            if i != j:
                payoffs[0], payoffs[1] = payoffs[1], payoffs[0]
                results[j][i] = payoffs


    sort_strategies(strategies, results)
    print_results(strategies, results)


def sort_strategies(strategies, results):
    N = len(strategies)

    for j in range(1, N):
        for i in range(N - j):
            if calculate_sum_of_payoffs(results[i]) < calculate_sum_of_payoffs(results[i + 1]):
                strategies[i], strategies[i + 1] = strategies[i + 1], strategies[i]
                for k in range(N):
                    results[i][k], results[i + 1][k] = results[i + 1][k], results[i][k]
                for k in range(N):
                    results[k][i], results[k][i + 1] = results[k][i + 1], results[k][i]


def swap_payoffs(payoff):
    payoff[0], payoff[1] = payoff[1], payoff[0]


def calculate_sum_of_payoffs(strategy_results):
    return sum([result[0] for result in strategy_results])


def print_results(strategies, results):
    N = len(strategies)
    table = [[None] * (N + 2) for _ in range(N + 1)]
    for i in range(N):
        table[0][i + 1] = strategies[i].__name__
        table[i + 1][0] = strategies[i].__name__
    table[0][-1] = 'SUM'

    for i in range(N):
        for j in range(N):
            table[i + 1][j + 1] = results[i][j]

    for i in range(N):
        table[i + 1][-1] = calculate_sum_of_payoffs(results[i])

    print(tabulate(table))
    
    
if __name__ == '__main__':
    main()
