import json
import pandas as pd

# File Path
json_path = '/Users/Study/avHubert/TCD-TIMIT/volunteer/large_vol_av_433_-20/hypo-244018.json'
csv_path = '/Users/Study/avHubert/TCD-TIMIT/volunteer/large_vol_av_433_-20/hypo-244018.csv'

# Read JSON
with open(json_path, 'r') as f:
    data = json.load(f)

print(data.keys())

# Transfer to DataFrame
df = pd.DataFrame(data)

df.to_csv(csv_path, index=False)

print(f'✅ 已保存 CSV 文件到: {csv_path}')