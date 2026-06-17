import os

import matplotlib.pyplot as plt
import numpy as np

from src.config import ALGORITHMS, FIGURES_DIR, INSTANCES, N_RUNS

COLORS = {
    "RNN": "#4C72B0",
    "RNN-SA": "#DD8452",
    "RNN-SA-Reheating": "#55A868",
}


def _ensure_dir():
    os.makedirs(FIGURES_DIR, exist_ok=True)


def generate_best_costs_bar(summary_df):
    _ensure_dir()

    instance_names = list(INSTANCES.keys())
    x = np.arange(len(instance_names))
    width = 0.25

    fig, ax = plt.subplots(figsize=(10, 5))

    for i, algo in enumerate(ALGORITHMS):
        subset = summary_df[summary_df["algorithm"] == algo]
        subset = subset.set_index("instance").reindex(instance_names)
        bars = ax.bar(
            x + (i - 1) * width,
            subset["best"],
            width,
            label=algo,
            color=COLORS[algo],
        )

    # linha do ótimo por instância
    for j, inst in enumerate(instance_names):
        optimal = INSTANCES[inst]["optimal"]
        ax.hlines(
            optimal,
            j - 1.5 * width,
            j + 1.5 * width,
            colors="red",
            linestyles="--",
            linewidth=1.2,
        )

    ax.set_xticks(x)
    ax.set_xticklabels(instance_names)
    ax.set_ylabel("Melhor custo encontrado")
    ax.set_title("Melhor custo por instância e algoritmo\n(linha vermelha = ótimo conhecido)")
    ax.legend()
    plt.tight_layout()
    path = os.path.join(FIGURES_DIR, "best_costs_comparison.png")
    fig.savefig(path, dpi=300)
    plt.close(fig)
    print(f"  Salvo: {path}")


def generate_boxplots(raw_df):
    _ensure_dir()

    for instance_name, meta in INSTANCES.items():
        fig, ax = plt.subplots(figsize=(7, 5))

        data = [
            raw_df[
                (raw_df["instance"] == instance_name)
                & (raw_df["algorithm"] == algo)
            ]["cost"].values
            for algo in ALGORITHMS
        ]

        bp = ax.boxplot(
            data,
            labels=ALGORITHMS,
            patch_artist=True,
            medianprops={"color": "black", "linewidth": 1.5},
        )

        for patch, algo in zip(bp["boxes"], ALGORITHMS):
            patch.set_facecolor(COLORS[algo])
            patch.set_alpha(0.7)

        ax.axhline(
            meta["optimal"],
            color="red",
            linestyle="--",
            linewidth=1.2,
            label=f"Ótimo = {meta['optimal']}",
        )

        ax.set_ylabel("Custo do tour")
        ax.set_title(f"Distribuição de custos — {instance_name} ({N_RUNS} rodadas)")
        ax.legend()
        plt.tight_layout()
        path = os.path.join(FIGURES_DIR, f"boxplot_{instance_name}.png")
        fig.savefig(path, dpi=300)
        plt.close(fig)
        print(f"  Salvo: {path}")


def generate_convergence_curves(convergence_data):
    _ensure_dir()

    for instance_name, histories in convergence_data.items():
        if not histories:
            continue

        fig, ax = plt.subplots(figsize=(9, 5))

        for algo, history in histories.items():
            ax.plot(history, label=algo, color=COLORS[algo], linewidth=1.2)

        optimal = INSTANCES[instance_name]["optimal"]
        ax.axhline(
            optimal,
            color="red",
            linestyle="--",
            linewidth=1.0,
            label=f"Ótimo = {optimal}",
        )

        ax.set_xlabel("Iteração")
        ax.set_ylabel("Melhor custo encontrado")
        ax.set_title(f"Curva de convergência — {instance_name}")
        ax.legend()
        plt.tight_layout()
        path = os.path.join(FIGURES_DIR, f"convergence_{instance_name}.png")
        fig.savefig(path, dpi=300)
        plt.close(fig)
        print(f"  Salvo: {path}")


def generate_all_figures(raw_df, summary_df, convergence_data):
    print("\nGerando figuras...")
    generate_best_costs_bar(summary_df)
    generate_boxplots(raw_df)
    generate_convergence_curves(convergence_data)

