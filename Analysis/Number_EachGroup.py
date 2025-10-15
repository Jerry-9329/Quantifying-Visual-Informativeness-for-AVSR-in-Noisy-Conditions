import pandas as pd

# Load Data
df = pd.read_csv("/Users/Study/avHubert/TCD-TIMIT/Combine_v_433/common_words_IWER_MaFI_with_diff_resample.csv")

# Set the MaFI threshold
lower_threshold = -1.1728
upper_threshold = -0.8448

group_high = df[df['MaFI_lip'] > upper_threshold].shape[0]
group_mid = df[(df['MaFI_lip'] <= upper_threshold) & (df['MaFI_lip'] >= lower_threshold)].shape[0]
group_low = df[df['MaFI_lip'] < lower_threshold].shape[0]

print("High MaFI（> -0.8448）:", group_high)
print("Medium MaFI（-1.1728 ~ -0.8448）:", group_mid)
print("Low MaFI（< -1.1728）:", group_low)