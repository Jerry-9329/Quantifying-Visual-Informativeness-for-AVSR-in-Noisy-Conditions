import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

snr_values = [-15, -10, -5, 0, 5, 10, 15]
Pearson = [-0.246, -0.203, -0.158, -0.118, -0.089, -0.075, -0.075]

red = [0, 1, 2, 3]
# green = [0, 1, 2, 5]

plt.plot(snr_values, Pearson, marker='o', color = 'blue')

# Draw each point and specify the color according to the index
for i, (x, y) in enumerate(zip(snr_values, Pearson)):
    if i in red:
        color = 'red'
    # elif i in green:
    #     color = 'green'
    else:
        color = 'blue'
    plt.plot(x, y, marker='o', color=color)

legend_elements = [
    Line2D([0], [0], marker='o', color='w', label='p < 0.001', markerfacecolor='red', markersize=8),
    Line2D([0], [0], marker='o', color='w', label='0.001< p < 0.01', markerfacecolor='green', markersize=8),
    Line2D([0], [0], marker='o', color='w', label='p > 0.01', markerfacecolor='blue', markersize=8),
]

plt.legend(handles=legend_elements, loc='upper left')

# Plot
# plt.plot(snr_values, Pearson, marker='o')
plt.title('LRS2 Training Set')
plt.xlabel('SNR (dB)')
plt.ylabel('Pearson Correlation')
# plt.grid(True)

output_path = "/Users/Study/Speech_Recognition/Final_Thesis/Fig/Chapter4/raster/LRS2_Train_Pearson.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Figure save to {output_path}")

plt.show()