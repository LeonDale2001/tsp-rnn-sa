from src.rnn import repetitive_nearest_neighbor
from src.sa import simulated_annealing
from src.tsp import load_instance


def main():

    print("=" * 50)
    print("TSP-RNN-SA")
    print("=" * 50)

    instance_path = "data/eil51.tsp"

    problem = load_instance(instance_path)

    print(f"\nInstância: {problem.name}")
    print(f"Número de cidades: {problem.dimension}")

    print("\nExecutando RNN...")

    routes = repetitive_nearest_neighbor(
        problem
    )

    best_rnn = routes[0]

    print(
        f"Melhor custo RNN: "
        f"{best_rnn['cost']:.2f}"
    )

    print("\nExecutando RNN-SA...")

    _, sa_cost = simulated_annealing(
        problem,
        best_rnn["route"],
    )

    print(
        f"Melhor custo RNN-SA: "
        f"{sa_cost:.2f}"
    )

    print(
        "\nExecutando "
        "RNN-SA + Reheating..."
    )

    _, sa_reheating_cost = simulated_annealing(
        problem,
        best_rnn["route"],
        reheating=True,
        stagnation_limit=100,
        reheating_factor=2.0,
    )

    print(
        f"Melhor custo "
        f"RNN-SA-Reheating: "
        f"{sa_reheating_cost:.2f}"
    )

    print("\nComparação:")

    print(
        f"RNN              : "
        f"{best_rnn['cost']:.2f}"
    )

    print(
        f"RNN-SA           : "
        f"{sa_cost:.2f}"
    )

    print(
        f"RNN-SA-Reheating : "
        f"{sa_reheating_cost:.2f}"
    )


if __name__ == "__main__":
    main()