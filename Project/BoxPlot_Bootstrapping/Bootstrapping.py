import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter


def bootstrap_mafi_iwer(df, n_iterations, sample_size, seed=42):
    bins = [-np.inf, -1.1728, -0.8448, np.inf]
    labels = ['Low', 'Medium', 'High']
    df = df.copy()
    df['MaFI_Group'] = pd.cut(df['MaFI'], bins=bins, labels=labels)

    # Bootstrapping
    rng = np.random.default_rng(seed)
    boot_results = {label: [] for label in labels}

    for group in labels:
        group_data = df[df['MaFI_Group'] == group]['IWER'].values
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


import seaborn as sns


def plot_boxplot_distributions(boot_df, title="Lip Speakers"):
    plt.figure(figsize=(10, 6))
    boot_long = boot_df.melt(var_name="MaFI Group", value_name="IWER")

    sns.boxplot(x="MaFI Group", y="IWER", data=boot_long, palette="Set3")
    plt.title(title)
    plt.ylabel("IWER")
    plt.xlabel("MaFI Group")
    plt.ylim(0, 1)
    plt.gca().yaxis.set_major_formatter(PercentFormatter(xmax=1, decimals=0))
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    # save_path = "/Users/Study/Speech_Recognition/Final_Thesis/Fig/Chapter5/raster/LipSpeakers.png"
    # plt.savefig(save_path, dpi=300, bbox_inches='tight')
    # print(f"Figure save to {save_path}")
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv("/Users/Study/avHubert/Resample_40/TCD-TIMIT/Vol/-15/IWER_MaFI_6_resample_-15_2.csv")

    boot_df = bootstrap_mafi_iwer(df, 100, 20) # 100, 20

    summary_df = summarize_bootstrap_results(boot_df)

    plot_boxplot_distributions(boot_df)
    print(summary_df.transpose())