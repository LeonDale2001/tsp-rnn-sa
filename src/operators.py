import random


def swap(route):
    new_route = route.copy()

    i, j = random.sample(range(len(route)), 2)

    new_route[i], new_route[j] = (
        new_route[j],
        new_route[i],
    )

    return new_route


def reversion(route):
    new_route = route.copy()

    i, j = sorted(
        random.sample(range(len(route)), 2)
    )

    new_route[i:j + 1] = reversed(
        new_route[i:j + 1]
    )

    return new_route


def insertion(route):
    new_route = route.copy()

    i, j = random.sample(range(len(route)), 2)

    city = new_route.pop(i)

    new_route.insert(j, city)

    return new_route