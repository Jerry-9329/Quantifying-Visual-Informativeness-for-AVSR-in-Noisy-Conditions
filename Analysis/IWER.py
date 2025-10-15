import pandas as pd
from collections import defaultdict

# --------------------------
# 1. Levenshtein align
# --------------------------
def levenshtein_alignment(ref, hyp):
    n, m = len(ref), len(hyp)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    backtrace = [[None] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i
        backtrace[i][0] = 'del'
    for j in range(m + 1):
        dp[0][j] = j
        backtrace[0][j] = 'ins'
    backtrace[0][0] = None

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if ref[i - 1] == hyp[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
                backtrace[i][j] = 'ok'
            else:
                sub_cost = dp[i - 1][j - 1] + 1
                ins_cost = dp[i][j - 1] + 1
                del_cost = dp[i - 1][j] + 1
                dp[i][j] = min(sub_cost, ins_cost, del_cost)

                if dp[i][j] == sub_cost:
                    backtrace[i][j] = 'sub'
                elif dp[i][j] == ins_cost:
                    backtrace[i][j] = 'ins'
                else:
                    backtrace[i][j] = 'del'

    i, j = n, m
    ops = []
    while i > 0 or j > 0:
        op = backtrace[i][j]
        if op == 'ok' or op == 'sub':
            ops.append((op, ref[i - 1], hyp[j - 1]))
            i -= 1
            j -= 1
        elif op == 'del':
            ops.append((op, ref[i - 1], None))
            i -= 1
        elif op == 'ins':
            ops.append((op, None, hyp[j - 1]))
            j -= 1
    return ops[::-1]

# --------------------------
# 2. Main Function：Calculate IWER for each word
# --------------------------
def compute_word_iwer(df, ref_col="ref", hypo_col="hypo"):
    substitutions = defaultdict(int)
    deletions = defaultdict(int)
    occurrences = defaultdict(int)

    for _, row in df.iterrows():
        ref_words = row[ref_col].strip().split()
        hyp_words = row[hypo_col].strip().split()
        alignment = levenshtein_alignment(ref_words, hyp_words)

        for op, ref_w, hyp_w in alignment:
            if op == "ok":
                occurrences[ref_w] += 1
            elif op == "sub":
                substitutions[ref_w] += 1
                occurrences[ref_w] += 1
            elif op == "del":
                deletions[ref_w] += 1
                occurrences[ref_w] += 1

    iwer_data = []
    for word in occurrences:
        total_errors = substitutions[word] + deletions[word]
        iwer = total_errors / occurrences[word]
        iwer_data.append({
            "word": word,
            "occurrences": occurrences[word],
            "substitutions": substitutions[word],
            "deletions": deletions[word],
            "IWER": round(iwer, 4)
        })

    return pd.DataFrame(iwer_data).sort_values(by="IWER", ascending=False)


if __name__ == "__main__":
    # Load CSV
    df = pd.read_csv("/Users/Study/avHubert/TCD-TIMIT/large_Lip_av_433_-15/hypo-244018.csv")

    word_iwer_df = compute_word_iwer(df, ref_col="ref", hypo_col="hypo")

    word_iwer_df.to_csv("/Users/Study/avHubert/TCD-TIMIT/large_Lip_av_433_-15/IWER.csv", index=False)
    print(word_iwer_df.head())