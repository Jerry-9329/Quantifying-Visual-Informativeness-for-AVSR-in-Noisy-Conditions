import pandas as pd

# Read files
df = pd.read_csv('/Users/Study/avHubert/Resample_40/TCD-TIMIT/Overlap/-10/common_words_IWER_MaFI_resample.csv')

# Calculate difference
df['IWER_diff'] = df['IWER_lip'] - df['IWER_vol']

# Save
df.to_csv('/Users/Study/avHubert/Resample_40/TCD-TIMIT/Overlap/-10/common_words_IWER_MaFI_resample_diff_-5.csv', index=False)

print("Finish: common_words_IWER_MaFI_with_diff.csv")