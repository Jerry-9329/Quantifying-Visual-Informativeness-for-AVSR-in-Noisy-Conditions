import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('/Users/Study/Python_Help/MaFI/Norms/MaFI_Combined.csv')

# Plot the histogram of MaFI distribution (30 bins)
plt.figure(figsize=(10, 6))
plt.hist(df['MaFI'], bins=30, edgecolor='black', alpha=0.7)
plt.title('MaFI Database', fontsize=22)
plt.xlabel('MaFI Score', fontsize=20)
plt.ylabel('Frequency', fontsize=20)
# plt.grid(True)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.tight_layout()

output_path = "/Users/Study/Speech_Recognition/Final_Thesis/Fig/Chapter3/raster/MaFIDatabase.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Figure saved to {output_path}")

plt.show()

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
#
# df = pd.read_csv('/Users/Study/avHubert/LRS2_train/large_av_433_0/IWER_MaFI_6_0.csv')
# df_combined = pd.read_csv('/Users/Study/Python_Help/MaFI/Norms/MaFI_Combined.csv')
# bins = np.histogram_bin_edges(df_combined['MaFI'], bins=30)
#
# plt.figure(figsize=(10, 6))
# plt.hist(df['MaFI'], bins=bins, edgecolor='black', alpha=0.7)
# plt.title('LRS2 Training Set', fontsize=22)
# plt.xlabel('MaFI Score', fontsize=20)
# plt.ylabel('Frequency', fontsize=20)
#
# plt.xticks(fontsize=20)
# plt.yticks(fontsize=20)
#
# plt.tight_layout()
#
# output_path = "/Users/Study/Speech_Recognition/Final_Thesis/Fig/Chapter3/raster/LRS2Train.png"
# plt.savefig(output_path, dpi=300, bbox_inches='tight')
# print(f"Figure saved to {output_path}")
#
# plt.show()