import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import PercentFormatter


def bootstrap_column(df, column, n_iterations, sample_size, seed=42):
    bins = [-np.inf, -1.1728, -0.8448, np.inf]
    labels = ['Low', 'Medium', 'High']
    df = df.copy()
    df['MaFI_Group'] = pd.cut(df['MaFI_lip'], bins=bins, labels=labels)

    rng = np.random.default_rng(seed)
    boot_results = {label: [] for label in labels}

    for group in labels:
        group_data = df[df['MaFI_Group'] == group][column].values
        if len(group_data) < sample_size:
            print(f"Warning: group '{group}' has fewer samples ({len(group_data)}) than sample_size ({sample_size})")

        for _ in range(n_iterations):
            sample = rng.choice(group_data, size=sample_size, replace=True)
            boot_results[group].append(np.mean(sample))

    return pd.DataFrame(boot_results)

def summarize_bootstrap_results(boot_df):
    summary = {}
    for group in boot_df.columns:
        data = boot_df[group]
        summary[group] = {
            'Mean': np.mean(data),
            'Median': np.median(data),
            'Variance': np.var(data, ddof=1)
        }
    return pd.DataFrame(summary)

def plot_separate_boxplots(all_boot_dfs, metric_titles, ylims, ylabels):
    fig, axes = plt.subplots(1, 3, figsize=(20, 6))  # 不共享 y 轴

    for ax, (metric, boot_df) in zip(axes, all_boot_dfs.items()):
        boot_long = boot_df.melt(var_name="MaFI Group", value_name=metric)
        sns.boxplot(x="MaFI Group", y=metric, data=boot_long, palette="Set3", ax=ax)
        ax.yaxis.set_major_formatter(PercentFormatter(xmax=1, decimals=0))
        ax.set_title(metric_titles[metric])
        ax.set_xlabel("MaFI Group")
        ax.set_ylabel(ylabels[metric])
        if metric in ylims:
            ax.set_ylim(ylims[metric])
        ax.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()

    # output_path = "/Users/Study/Speech_Recognition/Final_Thesis/Fig/Chapter5/raster/Diff_Vol_Lip.png"
    # fig.savefig(output_path, dpi=300, bbox_inches='tight')
    # print(f"Figure save to {output_path}")

    plt.show()

if __name__ == "__main__":
    df = pd.read_csv("/Users/Study/avHubert/TCD-TIMIT/Combine_v_433/common_words_IWER_MaFI_with_diff_resample.csv")

    # Title
    metrics = {
        "IWER_lip":  "Lip Speakers",
        "IWER_vol":  "Volunteers",
        "IWER_diff": "Difference (Vol-Lip)",
    }

    # Range of y
    ylims = {
        "IWER_lip":  (0, 0.6),
        "IWER_vol":  (0, 0.6),
        "IWER_diff": (-0.4, 0),
    }


    ylabels = {
        "IWER_lip":  "IWER",
        "IWER_vol":  "IWER",
        "IWER_diff": "IWER",
    }

    # Bootstrapping & Summary
    all_boot_dfs = {}
    for metric in metrics:
        boot_df = bootstrap_column(df, metric, n_iterations=100, sample_size=20)
        summary_df = summarize_bootstrap_results(boot_df)
        all_boot_dfs[metric] = boot_df
        print(f"\n=== Summary for {metric} ===")
        print(summary_df.transpose())


    plot_separate_boxplots(all_boot_dfs, metrics, ylims, ylabels)