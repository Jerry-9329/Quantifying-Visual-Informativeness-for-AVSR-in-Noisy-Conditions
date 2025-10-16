import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

snr_values = [-25, -20, -15, -10, -5, 0, 5, 10, 15]
Pearson = [-0.123, -0.108, -0.086, -0.075, -0.058, 0.033, 0.012, 0.039, 0.018]

legend_elements = [
    Line2D([0], [0], marker='o', color='w', label='p < 0.001', markerfacecolor='red', markersize=8),
    Line2D([0], [0], marker='o', color='w', label='0.001< p < 0.01', markerfacecolor='green', markersize=8),
    Line2D([0], [0], marker='o', color='w', label='p > 0.01', markerfacecolor='blue', markersize=8),
]

plt.legend(handles=legend_elements, loc='upper left')

plt.plot(snr_values, Pearson, marker='o', color = 'blue')
plt.title('LRS3 Test Set')
plt.xlabel('SNR (dB)')
plt.ylabel('Pearson Correlation')
# plt.grid(True)

output_path = "/Users/Study/Speech_Recognition/Final_Thesis/Fig/Chapter4/raster/LRS3_Test_Pearson.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Figure save to {output_path}")

plt.show()

# import matplotlib.pyplot as plt
# from matplotlib.patches import FancyArrowPatch
#
# # 数据
# snr_values = [-25, -20, -15, -10, -5, 0, 5, 10, 15]
# # Pearson = [-0.123, -0.108, -0.086, -0.075, -0.058, 0.033, 0.012, 0.039, 0.018]
# Pearson = [-0.123, -0.108, -0.086, -0.075, -0.058, 0.033, 0.012, 0.039, 0.018]
#
#
# # 创建图形
# fig, ax = plt.subplots(figsize=(8, 5))
# ax.plot(snr_values, Pearson, marker='o', label='Pearson Correlation')
#
# # 添加垂直线
# ax.axvline(x=-5, color='red', linestyle='--', linewidth=2, label='SNR = -5 dB')
# ax.axvline(x=5, color='green', linestyle='--', linewidth=2, label='SNR = 5 dB')
#
# # 添加双向箭头表示 SNR < -5 区间
# arrow = FancyArrowPatch(
#     posA=(-25, 0.02), posB=(-5, 0.02),  # 起点和终点
#     arrowstyle='<->', linewidth=2, mutation_scale=10, color='red'
# )
# ax.add_patch(arrow)
#
# arrow2 = FancyArrowPatch(
#     posA=(5, -0.08), posB=(15, -0.08),  # 起点和终点
#     arrowstyle='<->', linewidth=2, mutation_scale=10, color='green'
# )
# ax.add_patch(arrow2)
#
# # 添加文字注释
# ax.text(-20, 0.023, 'SNR ≤ -5', color='red', fontsize=13, fontweight='bold')
# ax.text(8, -0.078, 'SNR ≥ 5', color='green', fontsize=13, fontweight='bold')
#
# # 标题与标签
# ax.set_title('LRS3 Test Set')
# ax.set_xlabel('SNR (dB)')
# ax.set_ylabel('Pearson Correlation')
# ax.legend()
# plt.tight_layout()
# plt.show()