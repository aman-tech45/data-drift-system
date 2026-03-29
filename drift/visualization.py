import matplotlib.pyplot as plt
import os

def plot_feature_distribution(ref_df, cur_df, output_dir="plots"):
    os.makedirs(output_dir, exist_ok=True)

    for col in ref_df.columns:
        plt.figure()

        # Plot histograms
        plt.hist(ref_df[col], bins=10, alpha=0.5, label="Reference", density=True)
        plt.hist(cur_df[col], bins=10, alpha=0.5, label="Current", density=True)

        plt.title(f"Distribution Comparison: {col}")
        plt.xlabel(col)
        plt.ylabel("Density")
        plt.legend()

        # Save plot
        file_path = os.path.join(output_dir, f"{col}_distribution.png")
        plt.savefig(file_path)

        plt.close()