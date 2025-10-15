import pandas as pd, pronouncing, re, seaborn as sns
import matplotlib.pyplot as plt
from collections import defaultdict
from matplotlib.ticker import PercentFormatter

# Viseme mapping
VIS_MAP = {
    "LowerLipTuck": ['F', 'V'],
    "LipRounding": ['R', 'Y', 'W'],
    "LabialClosure": ['P', 'B', 'M'],
    "Protrusion": ['SH', 'CH', 'JH', 'W'],
}
# viseme_order = ["LowerLipTuck", "LipRounding", "LabialClosure", "Protrusion"]
viseme_order = ["Protrusion", "LabialClosure", "LipRounding", "LowerLipTuck"]

# File paths and labels to process
CSV_PATHS = {
    "Visual Only": "/Users/Study/avHubert/LRS2_train/large_v_433/IWER_MaFI_6_v.csv",
    "-15 dB (AV)": "/Users/Study/avHubert/LRS2_train/large_av_433_-15/IWER_MaFI_6_-15.csv",
    "0 dB (AV)": "/Users/Study/avHubert/LRS2_train/large_av_433_0/IWER_MaFI_6_0.csv",
    "15 dB (AV)": "/Users/Study/avHubert/LRS2_train/large_av_433_15/IWER_MaFI_6_15.csv",
}

# Collect all data
all_data = []

for model_name, csv_path in CSV_PATHS.items():
    df = pd.read_csv(csv_path)
    df["IWER"] = pd.to_numeric(df["IWER"], errors="coerce")
    viseme_word_iwer = defaultdict(list)

    for _, row in df.iterrows():
        word = str(row["word"]).lower()
        iwer = row["IWER"]
        for phones_raw in pronouncing.phones_for_word(word):
            phones = [re.sub(r"\d", "", p) for p in phones_raw.split()]
            for viseme, phonemes in VIS_MAP.items():
                if any(ph in phones for ph in phonemes):
                    viseme_word_iwer[viseme].append((word, iwer))

    viseme_df = pd.DataFrame([
        {"Viseme": v, "Word": w, "IWER": iwer, "Mode": model_name}
        for v, lst in viseme_word_iwer.items()
        for w, iwer in lst
    ]).dropna()

    all_data.append(viseme_df)

# Merge all data across modes
full_df = pd.concat(all_data, ignore_index=True)
full_df["Viseme"] = pd.Categorical(full_df["Viseme"], categories=viseme_order, ordered=True)

# ---------- Faceted Boxplot ----------
g = sns.catplot(
    data=full_df,
    x="Viseme",
    y="IWER",
    col="Mode",
    kind="box",
    col_wrap=2,
    height=4,
    aspect=1.1,
    palette="Set2",
    sharey=True
)

g.fig.subplots_adjust(top=0.88)
g.fig.suptitle("LRS2 Training Set", fontsize=16)

for ax in g.axes.flatten():
    ax.set_title(ax.get_title().replace("Mode = ", ""))
    ax.yaxis.set_major_formatter(PercentFormatter(xmax=1, decimals=0))
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.set_xlabel("Viseme")
    ax.set_ylabel("IWER")

plt.tight_layout()

# output_path = "/Users/Study/Speech_Recognition/Final_Thesis/Fig/Chapter4/raster/LRS2_Train_Viseme.png"
# g.savefig(output_path, dpi=300, bbox_inches='tight')
# print(f"Figure saved to {output_path}")

plt.show()

viseme_counts = full_df.groupby(["Mode", "Viseme"]).size().unstack(fill_value=0)
print(viseme_counts)

mean_iwer = full_df.groupby(["Mode", "Viseme"])["IWER"].mean().unstack()
print("Average IWER per Viseme in each mode:")
print(mean_iwer)