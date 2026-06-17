import math
import random

from src.rnn import route_cost
from src.operators import (
    swap,
    reversion,
    insertion,
)


def reheating_temperature(
    temperature: float,
    factor: float = 2.0,
) -> float:
    """
    Reaquece o sistema aumentando
    temporariamente a temperatura.
    """
    return temperature * factor


def generate_neighbor(route):
    """
    Seleciona um operador de vizinhança
    seguindo as probabilidades do artigo.

    Swap      -> 20%
    Reversion -> 50%
    Insertion -> 30%
    """

    r = random.random()

    if r < 0.2:
        return swap(route)

    elif r < 0.7:
        return reversion(route)

    return insertion(route)


def simulated_annealing(
    problem,
    initial_route,
    temperature=0.025,
    cooling=0.99,
    iterations=1000,
    reheating=False,
    stagnation_limit=100,
    reheating_factor=2.0,
    track_convergence=False,
):
    """
    Simulated Annealing.

    Se reheating=False:
        executa exatamente a versão base.

    Se reheating=True:
        utiliza a proposta de melhoria.
    """

    current_route = initial_route.copy()

    current_cost = route_cost(
        problem,
        current_route,
    )

    best_route = current_route.copy()
    best_cost = current_cost

    T = temperature

    stagnation = 0

    history = [] if track_convergence else None

    for _ in range(iterations):

        neighbor = generate_neighbor(
            current_route
        )

        neighbor_cost = route_cost(
            problem,
            neighbor,
        )

        delta = (
            neighbor_cost
            - current_cost
        )

        accepted = False

        if delta <= 0:

            accepted = True

        else:

            probability = math.exp(
                -delta / T
            )

            if random.random() < probability:
                accepted = True

        if accepted:

            current_route = neighbor
            current_cost = neighbor_cost

        if current_cost < best_cost:

            best_route = current_route.copy()
            best_cost = current_cost

            stagnation = 0

        else:

            stagnation += 1

        # ====================================
        # SUA CONTRIBUIÇÃO
        # ====================================

        if (
            reheating
            and stagnation >= stagnation_limit
        ):

            T = reheating_temperature(
                T,
                reheating_factor,
            )

            stagnation = 0

        # ====================================

        T *= cooling

        if history is not None:
            history.append(best_cost)

        if T < 1e-12:
            break

    if track_convergence:
        return best_route, best_cost, history
    return best_route, best_cost