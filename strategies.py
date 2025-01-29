import random as rnd


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


def period_punishment_2(your_history: list[str], opponent_history: list[str]) -> str:
    return _period_punishment_k(your_history, opponent_history, k=2)


def period_punishment_5(your_history: list[str], opponent_history: list[str]) -> str:
    return _period_punishment_k(your_history, opponent_history, k=5)


def period_punishment_10(your_history: list[str], opponent_history: list[str]) -> str:
    return _period_punishment_k(your_history, opponent_history, k=10)


def _period_punishment_k(your_history: list[str], opponent_history: list[str], k) -> str:
    return 'C' if all(move == 'C' for move in opponent_history[-k:]) else 'D'
