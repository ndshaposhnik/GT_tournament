from inspect import getmembers, isfunction
from tabulate import tabulate

import strategies


def main():
    strats = [
        function
        for (name, function) in getmembers(strategies, isfunction)
        if name[0] != '_'
    ]
    conduct_tournament(strats)


NUM_ROUNDS = 100
GAME_VERSION = 0 # 0 if R0, 1 if R1


# 0 -- cooperate
# 1 -- defect

R0 = [
    [(3, 3), (0, 5)],
    [(5, 0), (1, 1)],
]
    
R1 = [
    [(3, 3), (0, 8)],
    [(8, 0), (1, 1)],
]


def calculate_payoffs(x: int, y: int, game_version=0) -> (int, int):
    assert x in [0, 1]
    assert y in [0, 1]
    if game_version == 0:
        return R0[x][y]
    else:
        return R1[x][y]


def run_battle(strategy1, strategy2):
    history1 = []
    history2 = []
    payoffs = [0, 0]
    for round in range(NUM_ROUNDS):
        x = strategy1(merge_histories(history1, history2))
        y = strategy2(merge_histories(history2, history1))
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


def merge_histories(history1: list[int], history2: list[int]) -> list[int]:
    N = len(history1)
    assert N == len(history2)
    history = []
    for i in range(N):
        history.append(history1[i])
        history.append(history2[i])
    return history
    
    
if __name__ == '__main__':
    main()
