"""Gera apenas a figura illustration_eil51.png sem re-rodar os 360 experimentos."""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.config import SA_PARAMS
from src.rnn import repetitive_nearest_neighbor
from src.sa import simulated_annealing
from src.tsp import load_instance
from src.visualization import generate_illustration

problem = load_instance("data/eil51.tsp")
routes = repetitive_nearest_neighbor(problem)
best_rnn_route = routes[0]["route"]

params = SA_PARAMS["eil51"]

sa_route, _, _ = simulated_annealing(
    problem, best_rnn_route, reheating=False, track_convergence=True, **params
)
reh_route, _, _ = simulated_annealing(
    problem, best_rnn_route, reheating=True, track_convergence=True, **params
)

illustration_data = {
    "problem": problem,
    "RNN-SA": sa_route,
    "RNN-SA-Reheating": reh_route,
}

generate_illustration(illustration_data)
print("Concluído.")
