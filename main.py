from tsp import load_instance, get_coordinates


def main():
    print("=" * 50)
    print("TSP-RNN-SA")
    print("=" * 50)

    instance_path = "data/eil51.tsp"

    problem = load_instance(instance_path)

    print(f"\nInstância: {problem.name}")
    print(f"Número de cidades: {problem.dimension}")

    coordinates = get_coordinates(problem)

    print("\nPrimeiras 5 cidades:")

    for city_id, coord in list(coordinates.items())[:5]:
        print(f"Cidade {city_id}: {coord}")

    print("\nProjeto configurado com sucesso!")


if __name__ == "__main__":
    main()