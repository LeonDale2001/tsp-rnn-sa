import tsplib95


def load_instance(path: str):
    """
    Carrega uma instância TSPLIB.
    """
    return tsplib95.load(path)


def get_coordinates(problem):
    """
    Retorna um dicionário:
    {cidade: (x, y)}
    """
    return problem.node_coords