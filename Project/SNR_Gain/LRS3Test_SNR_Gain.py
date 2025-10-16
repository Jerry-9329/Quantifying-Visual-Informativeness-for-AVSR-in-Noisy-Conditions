import matplotlib.pyplot as plt

# Define the value of SNR (dB)
snr_values = [-15, -10, -5, 0, 5, 10, 15]
snr_values2 = [-15, -10, -5, 0, 5, 10, 15]
snr_values3 = [-15, -10, -5, 0, 5, 10, 15]



# wer_model_30h_a = [96.26, 64.42, 24.17, 9.99, 3.67, 2.58, 1.95]
# wer_model_30h_av = [20.30, 9.82, 4.83, 2.91, 2.22, 1.59, 1.46]

low_wer_model_433h_a = [98.76, 67.25, 22.68, 7.85, 2.36, 1.1, 0.95]
low_wer_model_433h_av = [17.95, 8.82, 3.6, 1.18, 0.82, 0.72, 0.44]

medium_wer_model_433h_a = [99.12, 62.64, 18.68, 4.75, 0.87, 0.26, 0.14]
medium_wer_model_433h_av = [14.61, 5.32, 1.35, 0.13, 0, 0, 0]

high_wer_model_433h_a = [98.92, 65.27, 20.89, 7.71, 2.55, 0.8, 0.71]
high_wer_model_433h_av = [14.26, 6.39, 1.33, 0.68, 0.17, 0.29, 0.1]



# Color mapping
colors = {"Model 30h": "blue", "Model 433h": "red"}

plt.figure(figsize=(8, 6))
plt.title("LRS3 Test Set")

# plt.plot(snr_values, wer_model_30h_a, '--', color=colors["Model 30h"], label="Model 30h (Audio-only)")
# plt.plot(snr_values, wer_model_30h_av, '-', color=colors["Model 30h"], label="Model 30h (Audio-Visual)")

# 绘制 Model 433h
plt.plot(snr_values, low_wer_model_433h_a, '--', color="red", label="Low MaFI (Audio-only)")
plt.plot(snr_values2, low_wer_model_433h_av, '-', color="red", label="Low MaFI (Audio-Visual)")

plt.plot(snr_values, medium_wer_model_433h_a, '--', color="blue", label="Medium MaFI (Audio-only)")
plt.plot(snr_values2, medium_wer_model_433h_av, '-', color="blue", label="Medium MaFI (Audio-Visual)")

plt.plot(snr_values, high_wer_model_433h_a, '--', color="green", label="High MaFI (Audio-only)")
plt.plot(snr_values2, high_wer_model_433h_av, '-', color="green", label="High MaFI (Audio-Visual)")


plt.annotate("", xy=(0, 7.85), xytext=(-9.07, 7.85),
             arrowprops=dict(arrowstyle="<->", color="red", lw=1))

plt.annotate("", xy=(0, 4.75), xytext=(-9.28, 4.75),
             arrowprops=dict(arrowstyle="<->", color="blue", lw=1))

plt.annotate("", xy=(0, 7.71), xytext=(-10.84, 7.71),
             arrowprops=dict(arrowstyle="<->", color="green", lw=1))

plt.annotate("9.07dB GAIN", xy=(-4.5, 7.85), xytext=(3, 48),
             arrowprops=dict(color="red", arrowstyle="->"))

plt.annotate("9.28dB GAIN", xy=(-4.64, 4.75), xytext=(7.5, 40),
             arrowprops=dict(color="blue", arrowstyle="->"))

plt.annotate("10.84dB GAIN", xy=(-5.42, 7.71), xytext=(0, 60),
             arrowprops=dict(color="green", arrowstyle="->"))

plt.xlabel("SNR (dB)")
plt.ylabel("IWER (%)")
plt.xlim(-15, 15)
plt.ylim(0, 100)
plt.grid(True)
plt.legend(loc="upper right")

output_path = "/Users/Study/Speech_Recognition/Final_Thesis/Fig/Chapter4/raster/LRS3_SNR_Gain.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Figure save to {output_path}")

plt.show()