import pandas as pd
from drift.detector import detect_drift
from drift.visualization import plot_feature_distribution

def main():
    # Load datasets
    ref = pd.read_csv("data/reference.csv")
    cur = pd.read_csv("data/current.csv")

    # Drift detection
    report = detect_drift(ref, cur)

    print("\n📊 DATA DRIFT REPORT\n")
    print(report)

    # Visualization
    plot_feature_distribution(ref, cur)

    print("\n📁 Plots saved in 'plots/' folder")

if __name__ == "__main__":
    main()