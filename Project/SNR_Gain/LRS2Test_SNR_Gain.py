import matplotlib.pyplot as plt

# Define the value of SNR (dB)
snr_values = [-15, -10, -5, 0, 5, 10, 15]
snr_values2 = [-15, -10, -5, 0, 5, 10, 15]
snr_values3 = [-15, -10, -5, 0, 5, 10, 15]



# wer_model_30h_a = [96.26, 64.42, 24.17, 9.99, 3.67, 2.58, 1.95]
# wer_model_30h_av = [20.30, 9.82, 4.83, 2.91, 2.22, 1.59, 1.46]

low_wer_model_433h_a = [99.84, 87.87, 40.42, 19.44, 10.06, 13, 5.67]
low_wer_model_433h_av = [28.69, 13.87, 7.38, 4.55, 3.16, 2.8, 1.71]

medium_wer_model_433h_a = [99.8, 83.14, 47.64, 21.52, 11.75, 12.79, 5.63]
medium_wer_model_433h_av = [27.68, 15.73, 6.59, 3.05, 1.86, 2.94, 1.05]

high_wer_model_433h_a = [99.72, 84.75, 41.5, 16.99, 8.06, 10.79, 3.36]
high_wer_model_433h_av = [18.53, 9.43, 3.18, 1.17, 1.08, 1.19, 0.93]



# Color mapping
colors = {"Model 30h": "blue", "Model 433h": "red"}

plt.figure(figsize=(8, 6))
plt.title("LRS2 Test Set")

# plt.plot(snr_values, wer_model_30h_a, '--', color=colors["Model 30h"], label="Model 30h (Audio-only)")
# plt.plot(snr_values, wer_model_30h_av, '-', color=colors["Model 30h"], label="Model 30h (Audio-Visual)")

plt.plot(snr_values, low_wer_model_433h_a, '--', color="red", label="Low MaFI (Audio-only)")
plt.plot(snr_values2, low_wer_model_433h_av, '-', color="red", label="Low MaFI (Audio-Visual)")

plt.plot(snr_values, medium_wer_model_433h_a, '--', color="blue", label="Medium MaFI (Audio-only)")
plt.plot(snr_values2, medium_wer_model_433h_av, '-', color="blue", label="Medium MaFI (Audio-Visual)")

plt.plot(snr_values, high_wer_model_433h_a, '--', color="green", label="High MaFI (Audio-only)")
plt.plot(snr_values2, high_wer_model_433h_av, '-', color="green", label="High MaFI (Audio-Visual)")


plt.annotate("", xy=(0, 19.44), xytext=(-11.88, 19.44),
             arrowprops=dict(arrowstyle="<->", color="red", lw=1))

plt.annotate("", xy=(0, 21.52), xytext=(-12.42, 21.52),
             arrowprops=dict(arrowstyle="<->", color="blue", lw=1))

plt.annotate("", xy=(0, 16.99), xytext=(-14.15, 16.99),
             arrowprops=dict(arrowstyle="<->", color="green", lw=1))

plt.annotate("11.88dB GAIN", xy=(-5.94, 19.44), xytext=(3, 48),
             arrowprops=dict(color="red", arrowstyle="->"))

plt.annotate("12.42dB GAIN", xy=(-6.21, 21.52), xytext=(0, 60),
             arrowprops=dict(color="blue", arrowstyle="->"))

plt.annotate("14.15dB GAIN", xy=(-7.07, 16.99), xytext=(7.5, 40),
             arrowprops=dict(color="green", arrowstyle="->"))

plt.xlabel("SNR (dB)")
plt.ylabel("IWER (%)")
plt.xlim(-15, 15)
plt.ylim(0, 100)
plt.grid(True)
plt.legend(loc="upper right")

output_path = "/Users/Study/Speech_Recognition/Final_Thesis/Fig/Chapter4/raster/LRS2_SNR_Gain.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Figure save to {output_path}")

plt.show()