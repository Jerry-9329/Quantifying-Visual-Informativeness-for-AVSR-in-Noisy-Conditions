import pandas as pd
import scipy.stats as stats

# 读取数据
file_path = "/Users/Study/avHubert/LRS2/large_av_433_0/IWER_6_MaFI_0_resample.csv"
df = pd.read_csv(file_path)

# 处理 NaN 和 无穷大值
df_cleaned = df.replace([float("inf"), float("-inf")], pd.NA).dropna(subset=["IWER", "MaFI"])

# 计算相关性
pearson_corr, p_value = stats.pearsonr(df["IWER"], df["MaFI"])


# 输出结果
print(f"Pearson Correlation: {pearson_corr}")
print(f"P-value: {p_value}")