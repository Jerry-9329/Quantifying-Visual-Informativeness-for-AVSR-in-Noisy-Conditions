import pandas as pd

# Read Files
df1 = pd.read_csv('/Users/Study/avHubert/TCD-TIMIT/large_Lip_av_433_-10/IWER_MaFI_6.csv')
df2 = pd.read_csv('/Users/Study/avHubert/TCD-TIMIT/volunteer/large_vol_av_433_-10/IWER_MaFI_6.csv')

# Combine two files, extract the same words
common_words = pd.merge(
    df1[['word', 'IWER', 'MaFI']],
    df2[['word', 'IWER', 'MaFI']],
    on='word',
    suffixes=('_lip', '_vol')
)

# Save
common_words.to_csv('/Users/Study/avHubert/Resample_40/TCD-TIMIT/Overlap/-10/common_words_IWER_MaFI.csv', index=False)

print("Finish: common_words_IWER_MaFI.csv")