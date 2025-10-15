import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load two data files
df = pd.read_csv('/Users/Study/avHubert/TCD-TIMIT/volunteer/large_vol_av_433_-15/IWER_MaFI_6.csv')           # Original Data
df_combined = pd.read_csv('/Users/Study/Python_Help/MaFI/Norms/MaFI_Combined.csv')   # Target Data

# Step 2: Define and extract MaFI intervals (bins) to match the target distribution
bins = np.histogram_bin_edges(df_combined['MaFI'], bins=28)

# Step 3: Calculate the histogram frequency and scale of the target dataset
combined_counts, _ = np.histogram(df_combined['MaFI'], bins=bins)
combined_proportions = combined_counts / combined_counts.sum()

# Step 4: Assign MaFI packets in the raw data
df['MaFI_group'] = pd.cut(df['MaFI'], bins=bins, labels=False, include_lowest=True)

# Step 5: Resampled the data to conform to the target MaFI distribution
resampled_df = pd.DataFrame()
for i, proportion in enumerate(combined_proportions):
    group_df = df[df['MaFI_group'] == i]
    sample_size = int(proportion * len(df))
    if len(group_df) > 0:
        sampled_group = group_df.sample(n=min(sample_size, len(group_df)), replace=True, random_state=42)
        resampled_df = pd.concat([resampled_df, sampled_group])


plt.figure(figsize=(10, 6))
plt.hist(resampled_df['MaFI'], bins=bins, edgecolor='black', alpha=0.7)
plt.xlabel('MaFI')
plt.ylabel('Frequency')
plt.title('Resampled MaFI Distribution Matching MaFI_Combined.csv')
plt.grid(axis='y', linestyle='--')
plt.tight_layout()
plt.show()



resampled_df.to_csv('/Users/Study/avHubert/Resample_40/TCD-TIMIT/Vol/-15/IWER_MaFI_6_resample_-15_2.csv', index=False)