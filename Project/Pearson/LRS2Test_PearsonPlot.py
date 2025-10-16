import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# 几个点的坐标
snr_values = [-25, -20, -15, -10, -5, 0, 5, 10, 15]
Pearson = [-0.251, -0.273, -0.265, -0.052, -0.047, -0.083, -0.022, -0.041, 0.037]

red = [4]
green = [0, 1, 2, 5]

plt.plot(snr_values, Pearson, marker='o', color = 'blue')  # 连线

# 绘制每个点，按索引指定颜色
for i, (x, y) in enumerate(zip(snr_values, Pearson)):
    if i in red:
        color = 'red'
    elif i in green:
        color = 'green'
    else:
        color = 'blue'
    plt.plot(x, y, marker='o', color=color)

legend_elements = [
    Line2D([0], [0], marker='o', color='w', label='p < 0.001', markerfacecolor='red', markersize=8),
    Line2D([0], [0], marker='o', color='w', label='0.001< p < 0.01', markerfacecolor='green', markersize=8),
    Line2D([0], [0], marker='o', color='w', label='p > 0.01', markerfacecolor='blue', markersize=8),
]

plt.legend(handles=legend_elements, loc='upper left')

# 画图
# plt.plot(snr_values, Pearson, marker='o')  # 使用圆点标记每个点
plt.title('LRS2 Test Set')
plt.xlabel('SNR (dB)')
plt.ylabel('Pearson Correlation')

output_path = "/Users/Study/Speech_Recognition/Final_Thesis/Fig/Chapter4/raster/LRS2_Test_Pearson.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"图像已保存为 {output_path}")

# plt.grid(True)
plt.show()

# import matplotlib.pyplot as plt
# from matplotlib.patches import FancyArrowPatch
#
# # 数据
# snr_values = [-25, -20, -15, -10, -5, 0, 5, 10, 15]
# Pearson = [-0.251, -0.273, -0.265, -0.052, -0.047, -0.083, -0.022, -0.041, 0.037]
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
#     posA=(5, -0.2), posB=(15, -0.2),  # 起点和终点
#     arrowstyle='<->', linewidth=2, mutation_scale=10, color='green'
# )
# ax.add_patch(arrow2)
#
# # 添加文字注释
# ax.text(-20, 0.03, 'SNR ≤ -5', color='red', fontsize=13, fontweight='bold')
# ax.text(8, -0.19, 'SNR ≥ 5', color='green', fontsize=13, fontweight='bold')
#
# # 标题与标签
# ax.set_title('LRS2 Test Set')
# ax.set_xlabel('SNR (dB)')
# ax.set_ylabel('Pearson Correlation')
# ax.legend()
# plt.tight_layout()
# plt.show()