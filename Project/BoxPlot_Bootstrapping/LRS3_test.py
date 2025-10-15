import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import matplotlib.patches as mpatches
from matplotlib.ticker import PercentFormatter

def bootstrap_mafi_iwer(df, n_iterations, sample_size, seed=42):
    bins = [-np.inf, -1.1728, -0.8448, np.inf]
    labels = ['Low', 'Medium', 'High']
    df = df.copy()
    df['MaFI_Group'] = pd.cut(df['MaFI'], bins=bins, labels=labels)

    rng = np.random.default_rng(seed)
    boot_records = []

    for group in labels:
        group_data = df[df['MaFI_Group'] == group]['IWER'].values
        if len(group_data) < sample_size:
            print(f"Warning: group '{group}' has fewer samples ({len(group_data)}) than sample_size ({sample_size})")

        for _ in range(n_iterations):
            sample = rng.choice(group_data, size=sample_size, replace=True)
            boot_records.append({'MaFI Group': group, 'IWER': np.mean(sample)})

    return pd.DataFrame(boot_records)

def plot_faceted_bootstrap_boxplot(combined_df):
    title_map = {
        "IWER_MaFI_6_resample_15.csv": "SNR 15dB (Audio-Visual)",
        "IWER_MaFI_6_resample_0.csv": "SNR 0dB (Audio-Visual)",
        "IWER_MaFI_6_resample_-15.csv": "SNR -15dB (Audio-Visual)",
        "IWER_MaFI_6_resample_visual.csv": "Visual Mode",
    }

    g = sns.catplot(
        data=combined_df,
        x="MaFI Group",
        y="IWER",
        col="Source",
        kind="box",
        col_wrap=2,
        sharey=False,
        height=4,
        aspect=1.1,
        palette="Set2"
    )

    # g.fig.subplots_adjust(top=0.9)
    # # g.fig.suptitle()
    g.fig.subplots_adjust(top=0.88)
    g.fig.suptitle("LRS3 Test Set", fontsize=16)

    for ax in g.axes.flatten():
        source_key = ax.get_title().replace("Source = ", "").strip()
        custom_title = title_map.get(source_key, source_key)
        ax.set_title(custom_title)

        # source_df = combined_df[combined_df["Source"] == source_key]
        # means = source_df.groupby("MaFI Group")["IWER"].mean()
        # positions = range(len(means))
        # ax.scatter(positions, means, color='black', label='Mean', zorder=3)

        if "SNR 15dB" in custom_title or "SNR 0dB" in custom_title:
            ax.set_ylim(0, 0.1)
        else:
            ax.set_ylim(0, 0.5)

        ax.yaxis.set_major_formatter(PercentFormatter(xmax=1, decimals=0))

        ax.grid(True, linestyle="--", alpha=0.6)
        ax.set_ylabel("IWER")
        ax.set_xlabel("MaFI Group")

    handles = [mpatches.Patch(color='black', label='Mean')]
    plt.tight_layout()

    output_path = "/Users/Study/Speech_Recognition/Final_Thesis/Fig/Chapter4/raster/LRS3_Test_Box.png"
    g.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Figure saved to {output_path}")

    plt.show()

if __name__ == "__main__":
    csv_files = [
        "/Users/Study/avHubert/Resample_40/LRS3/15/IWER_MaFI_6_resample_15.csv",
        "/Users/Study/avHubert/Resample_40/LRS3/0/IWER_MaFI_6_resample_0.csv",
        "/Users/Study/avHubert/Resample_40/LRS3/-15/IWER_MaFI_6_resample_-15.csv",
        "/Users/Study/avHubert/Resample_40/LRS3/Visual-Only/IWER_MaFI_6_resample_visual.csv"
    ]

    combined_df = pd.DataFrame()

    for path in csv_files:
        df = pd.read_csv(path)
        boot_df = bootstrap_mafi_iwer(df, n_iterations=100, sample_size=20)
        boot_df["Source"] = os.path.basename(path)
        combined_df = pd.concat([combined_df, boot_df], ignore_index=True)

    plot_faceted_bootstrap_boxplot(combined_df)