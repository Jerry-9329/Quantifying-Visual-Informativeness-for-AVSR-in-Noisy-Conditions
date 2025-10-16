import matplotlib.pyplot as plt

# Define the value of SNR (dB)
snr_values = [-15, -10, -5, 0, 5, 10, 15]
snr_values2 = [-15, -10, -5, 0, 5, 10, 15]
snr_values3 = [-15, -10, -5, 0, 5, 10, 15]



# wer_model_30h_a = [96.26, 64.42, 24.17, 9.99, 3.67, 2.58, 1.95]
# wer_model_30h_av = [20.30, 9.82, 4.83, 2.91, 2.22, 1.59, 1.46]

low_wer_model_433h_a = [99.95, 95.13, 69.86, 43.18, 26.68, 18.3, 14.45]
low_wer_model_433h_av = [55.18, 38.97, 25.68, 17.41, 12.81, 10.83, 9.53]

medium_wer_model_433h_a = [99.93, 94.44, 69, 42.44, 26.56, 18, 14.34]
medium_wer_model_433h_av = [51.62, 35.74, 23.17, 16.23, 12.63, 10.66, 9.61]

high_wer_model_433h_a = [99.92, 94.53, 68.33, 42.33, 26.29, 17.71, 13.54]
high_wer_model_433h_av = [44.25, 30.49, 19.39, 13.81, 10.75, 8.92, 8.1]



# Color mapping
colors = {"Model 30h": "blue", "Model 433h": "red"}

plt.figure(figsize=(8, 6))
plt.title("LRS2 Training Set")


# plt.plot(snr_values, wer_model_30h_a, '--', color=colors["Model 30h"], label="Model 30h (Audio-only)")
# plt.plot(snr_values, wer_model_30h_av, '-', color=colors["Model 30h"], label="Model 30h (Audio-Visual)")

plt.plot(snr_values, low_wer_model_433h_a, '--', color="red", label="Low MaFI (Audio-only)")
plt.plot(snr_values2, low_wer_model_433h_av, '-', color="red", label="Low MaFI (Audio-Visual)")

plt.plot(snr_values, medium_wer_model_433h_a, '--', color="blue", label="Medium MaFI (Audio-only)")
plt.plot(snr_values2, medium_wer_model_433h_av, '-', color="blue", label="Medium MaFI (Audio-Visual)")

plt.plot(snr_values, high_wer_model_433h_a, '--', color="green", label="High MaFI (Audio-only)")
plt.plot(snr_values2, high_wer_model_433h_av, '-', color="green", label="High MaFI (Audio-Visual)")


plt.annotate("", xy=(0, 43.18), xytext=(-11.30, 43.18),
             arrowprops=dict(arrowstyle="<->", color="red", lw=1))

plt.annotate("", xy=(0, 42.44), xytext=(-12.11, 42.44),
             arrowprops=dict(arrowstyle="<->", color="blue", lw=1))

plt.annotate("", xy=(0, 42.33), xytext=(-14.3, 42.33),
             arrowprops=dict(arrowstyle="<->", color="green", lw=1))

plt.annotate("11.30dB GAIN", xy=(-5.65, 43.18), xytext=(7.5, 50),
             arrowprops=dict(color="red", arrowstyle="->"))

plt.annotate("12.11dB GAIN", xy=(-6.5, 42.44), xytext=(2.5, 60),
             arrowprops=dict(color="blue", arrowstyle="->"))

plt.annotate("14.30dB GAIN", xy=(-7.1, 42.33), xytext=(-2.5, 80),
             arrowprops=dict(color="green", arrowstyle="->"))

plt.xlabel("SNR (dB)")
plt.ylabel("IWER (%)")
plt.xlim(-15, 15)
plt.ylim(0, 100)
plt.grid(True)
plt.legend(loc="upper right")

output_path = "/Users/Study/Speech_Recognition/Final_Thesis/Fig/Chapter4/raster/LRS2_Train_SNR_Gain.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Figure save to {output_path}")

plt.show()