import os

from src.config import FIGURES_DIR, RAW_CSV, RESULTS_DIR, SUMMARY_CSV
from src.experiments import run_all_experiments
from src.visualization import generate_all_figures


def main():
    os.makedirs(RESULTS_DIR, exist_ok=True)
    os.makedirs(FIGURES_DIR, exist_ok=True)

    print("=" * 55)
    print("TSP-RNN-SA  |  Experimento completo")
    print("=" * 55)

    raw_df, summary_df, convergence_data = run_all_experiments()

    raw_df.to_csv(RAW_CSV, index=False)
    print(f"\nResultados brutos salvos em: {RAW_CSV}")

    summary_df.to_csv(SUMMARY_CSV, index=False)
    print(f"Sumário salvo em: {SUMMARY_CSV}")

    generate_all_figures(raw_df, summary_df, convergence_data)

    print("\n" + "=" * 55)
    print("SUMÁRIO DOS RESULTADOS")
    print("=" * 55)

    col_order = [
        "instance", "algorithm",
        "best", "mean", "std", "worst",
        "optimal", "gap_best_%", "gap_mean_%",
        "mean_time_s",
    ]
    print(summary_df[col_order].to_string(index=False))


if __name__ == "__main__":
    main()
