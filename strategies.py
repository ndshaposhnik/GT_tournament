import random as rnd


# Every function in this file that is NOT a strategy should begin with an '_'.

# 0 -- cooperate
# 1 -- defect


def all_cooperate(history):
    return 0


def all_defect(history):
    return 1


def random(history):
    return 0 if rnd.randint(0, 1) else 1


def tit_for_tat(history):
    if not history:
        return 0
    return history[-1]


def grim_trigger(history):
    return _period_punishment_k(history, k=len(history)+1)


def period_punishment_2(history):
    return _period_punishment_k(history, k=2)


def period_punishment_5(history):
    return _period_punishment_k(history, k=5)


def period_punishment_10(history):
    return _period_punishment_k(history, k=10)


def _period_punishment_k(history: list[int], k: int):
    opponent_history = _get_opponent_history(history)
    return 0 if all(move == 0 for move in opponent_history[-k:]) else 1


def _split_history(history: list[int]) -> (list[int], list[int]):
    return (
        [history[i] for i in range(0, len(history), 2)],
        [history[i + 1] for i in range(0, len(history), 2)]
     )


def _get_opponent_history(history: list[int]) -> list[int]:
    return _split_history(history)[1]
