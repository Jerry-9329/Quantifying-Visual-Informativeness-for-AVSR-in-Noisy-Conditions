import pandas as pd
from jiwer import wer

# Read file
df = pd.read_csv("/Users/Study/avHubert/TCD-TIMIT/Volunteer_Complete_version_Straight/visual_only_mode/hypo-244018.csv")

# Stitch all the text together
all_ref = " ".join(df["ref"].astype(str))
all_hypo = " ".join(df["hypo"].astype(str))

# Calculated WER
overall_wer = wer(all_ref, all_hypo)

print(f"Overall WER: {overall_wer:.8f}")