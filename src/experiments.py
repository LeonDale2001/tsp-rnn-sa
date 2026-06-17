import time

import pandas as pd
from tqdm import tqdm

from src.config import INSTANCES, N_RUNS, SA_PARAMS
from src.rnn import repetitive_nearest_neighbor
from src.sa import simulated_annealing
from src.tsp import load_instance


def run_all_experiments():
    records = []
    convergence_data = {}

    for instance_name, meta in INSTANCES.items():
        print(f"\n[{instance_name}] Carregando instância...")
        problem = load_instance(meta["path"])

        routes = repetitive_nearest_neighbor(problem)
        best_rnn = routes[0]
        rnn_cost = best_rnn["cost"]
        best_rnn_route = best_rnn["route"]

        convergence_data[instance_name] = {}

        # RNN é determinístico — registra N_RUNS vezes para manter schema uniforme
        t0 = time.perf_counter()
        rnn_time = time.perf_counter() - t0
        for run in range(N_RUNS):
            records.append({
                "instance": instance_name,
                "algorithm": "RNN",
                "run": run,
                "cost": rnn_cost,
                "time_s": rnn_time,
            })

        params = SA_PARAMS[instance_name]

        # RNN-SA
        print(f"[{instance_name}] RNN-SA ({N_RUNS} rodadas)...")
        for run in tqdm(range(N_RUNS), leave=False):
            is_last = run == N_RUNS - 1
            t0 = time.perf_counter()
            result = simulated_annealing(
                problem,
                best_rnn_route,
                reheating=False,
                track_convergence=is_last,
                **params,
            )
            elapsed = time.perf_counter() - t0

            if is_last:
                _, cost, history = result
                convergence_data[instance_name]["RNN-SA"] = history
            else:
                _, cost = result

            records.append({
                "instance": instance_name,
                "algorithm": "RNN-SA",
                "run": run,
                "cost": cost,
                "time_s": elapsed,
            })

        # RNN-SA-Reheating
        print(f"[{instance_name}] RNN-SA-Reheating ({N_RUNS} rodadas)...")
        for run in tqdm(range(N_RUNS), leave=False):
            is_last = run == N_RUNS - 1
            t0 = time.perf_counter()
            result = simulated_annealing(
                problem,
                best_rnn_route,
                reheating=True,
                track_convergence=is_last,
                **params,
            )
            elapsed = time.perf_counter() - t0

            if is_last:
                _, cost, history = result
                convergence_data[instance_name]["RNN-SA-Reheating"] = history
            else:
                _, cost = result

            records.append({
                "instance": instance_name,
                "algorithm": "RNN-SA-Reheating",
                "run": run,
                "cost": cost,
                "time_s": elapsed,
            })

    raw_df = pd.DataFrame(records)

    agg = raw_df.groupby(["instance", "algorithm"])["cost"].agg(
        best="min",
        mean="mean",
        std="std",
        worst="max",
    ).reset_index()

    time_agg = (
        raw_df.groupby(["instance", "algorithm"])["time_s"]
        .mean()
        .reset_index()
        .rename(columns={"time_s": "mean_time_s"})
    )

    summary_df = agg.merge(time_agg, on=["instance", "algorithm"])

    optima = pd.DataFrame([
        {"instance": k, "optimal": v["optimal"]}
        for k, v in INSTANCES.items()
    ])
    summary_df = summary_df.merge(optima, on="instance")

    summary_df["gap_best_%"] = (
        (summary_df["best"] - summary_df["optimal"]) / summary_df["optimal"] * 100
    ).round(2)
    summary_df["gap_mean_%"] = (
        (summary_df["mean"] - summary_df["optimal"]) / summary_df["optimal"] * 100
    ).round(2)

    summary_df["mean"] = summary_df["mean"].round(2)
    summary_df["std"] = summary_df["std"].round(2)

    return raw_df, summary_df, convergence_data
