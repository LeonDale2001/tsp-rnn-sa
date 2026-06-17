from math import inf


def route_cost(problem, route):
    cost = 0

    for i in range(len(route) - 1):
        cost += problem.get_weight(route[i], route[i + 1])

    cost += problem.get_weight(route[-1], route[0])

    return cost


def nearest_neighbor(problem, start_city):
    cities = list(problem.get_nodes())

    route = [start_city]
    unvisited = set(cities)
    unvisited.remove(start_city)

    current = start_city

    while unvisited:
        next_city = min(
            unvisited,
            key=lambda city: problem.get_weight(current, city)
        )

        route.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    return route


def repetitive_nearest_neighbor(problem):
    routes = []

    for city in problem.get_nodes():
        route = nearest_neighbor(problem, city)

        routes.append(
            {
                "route": route,
                "cost": route_cost(problem, route)
            }
        )

    routes.sort(key=lambda x: x["cost"])

    return routes