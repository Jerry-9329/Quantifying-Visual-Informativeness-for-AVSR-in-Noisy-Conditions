import pandas as pd

# Read
file_path = "/Users/Study/avHubert/TCD-TIMIT/large_Lip_av_433_-15/IWER_MaFI.csv"
df = pd.read_csv(file_path)

# Filter the rows with occurrences >= 6
filtered_df = df[df['occurrences'] >= 6]

filtered_df.to_csv("/Users/Study/avHubert/TCD-TIMIT/large_Lip_av_433_-15/IWER_MaFI_6.csv", index=False)

print(filtered_df.head())