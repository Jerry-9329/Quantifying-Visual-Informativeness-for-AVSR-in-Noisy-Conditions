import pandas as pd

# Read
df1 = pd.read_csv('/Users/Study/avHubert/TCD-TIMIT/large_Lip_av_433_-15/IWER.csv')
df2 = pd.read_csv('/Users/Study/Python_Help/MaFI/Norms/MaFI_Combined.csv')

# Convert the word column to lowercase for easier matching
df1['word_lower'] = df1['word'].str.lower()
df2['word_lower'] = df2['Word'].str.lower()

# Obtain the common words in the two tables
common_words = set(df1['word_lower']).intersection(set(df2['word_lower']))

# Filter out the data corresponding to the words that appear in both tables
common_df1 = df1[df1['word_lower'].isin(common_words)]
common_df2 = df2[df2['word_lower'].isin(common_words)]

# Merge the table and keep the fields you need
merged_common = pd.merge(
    common_df1[['word', 'occurrences', 'substitutions', 'deletions', 'IWER', 'word_lower']],
    common_df2[['word_lower', 'MaFI']],
    on='word_lower',
    how='inner'
)

merged_common.drop(columns=['word_lower'], inplace=True)

print(merged_common)

merged_common.to_csv('/Users/Study/avHubert/TCD-TIMIT/large_Lip_av_433_-15/IWER_MaFI.csv', index=False)