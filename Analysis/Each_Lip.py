import pandas as pd
from jiwer import wer

# Load CSV
df = pd.read_csv("/Users/Study/avHubert/TCD-TIMIT/large_Lip_av_433_-15/hypo-244018.csv")

# Extract ID
df['speaker'] = df['utt_id'].apply(lambda x: x.split('/')[1])

# Calculate WER
def compute_total_wer(group):
    ref_concat = " ".join(group['ref'])
    hypo_concat = " ".join(group['hypo'])
    return wer(ref_concat, hypo_concat)

# WER for each speaker
total_wer_per_speaker = df.groupby('speaker').apply(compute_total_wer).reset_index()
total_wer_per_speaker.columns = ['speaker', 'Total_WER']

# Print result
print(total_wer_per_speaker)

for speaker in df['speaker'].unique():
    speaker_df = df[df['speaker'] == speaker]
    speaker_df.to_csv(f"Lip/{speaker}.csv", index=False)
