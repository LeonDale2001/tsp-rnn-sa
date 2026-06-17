INSTANCES = {
    "eil51": {"path": "data/eil51.tsp", "optimal": 426},
    "berlin52": {"path": "data/berlin52.tsp", "optimal": 7542},
    "st70": {"path": "data/st70.tsp", "optimal": 675},
    "kroA100": {"path": "data/kroA100.tsp", "optimal": 21282},
}

N_RUNS = 30

SA_PARAMS = {
    "eil51": {
        "temperature": 0.025,
        "cooling": 0.99,
        "iterations": 5_000,
        "stagnation_limit": 100,
        "reheating_factor": 2.0,
    },
    "berlin52": {
        "temperature": 0.025,
        "cooling": 0.99,
        "iterations": 5_000,
        "stagnation_limit": 100,
        "reheating_factor": 2.0,
    },
    "st70": {
        "temperature": 0.025,
        "cooling": 0.995,
        "iterations": 10_000,
        "stagnation_limit": 150,
        "reheating_factor": 2.0,
    },
    "kroA100": {
        "temperature": 0.025,
        "cooling": 0.995,
        "iterations": 15_000,
        "stagnation_limit": 200,
        "reheating_factor": 2.0,
    },
}

RESULTS_DIR = "results"
FIGURES_DIR = "results/figures"
RAW_CSV = "results/raw_results.csv"
SUMMARY_CSV = "results/summary.csv"

ALGORITHMS = ["RNN", "RNN-SA", "RNN-SA-Reheating"]
