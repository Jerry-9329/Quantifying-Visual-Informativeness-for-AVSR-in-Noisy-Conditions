import os
import librosa
import numpy as np
import soundfile as sf


def add_noise_to_audio(audio_path, snr_db, source_root, target_root):
    # Read audio files
    y, sr = librosa.load(audio_path, sr=None)

    # Calculate the power of the audio signal
    signal_power = np.mean(y ** 2)

    # Calculate the noise power based on SNR
    noise_power = signal_power / (10 ** (snr_db / 10))

    # Generate Gaussian white noise
    noise = np.random.normal(0, np.sqrt(noise_power), y.shape)

    # Add noise to the audio signal
    y_noisy = y + noise

    rel_path = os.path.relpath(audio_path, source_root)
    noisy_rel_path = rel_path.replace(".wav", f".wav")
    noisy_audio_path = os.path.join(target_root, noisy_rel_path)

    os.makedirs(os.path.dirname(noisy_audio_path), exist_ok=True)

    sf.write(noisy_audio_path, y_noisy, sr)

    print(f"Finish: {audio_path} -> {noisy_audio_path}")


def process_lrs3_test(source_root, target_root, snr_db):
    for root, _, files in os.walk(source_root):
        for file in files:
            if file.startswith("._"):  # Skip macOS
                continue
            if file.endswith(".wav"):
                file_path = os.path.join(root, file)
                add_noise_to_audio(file_path, snr_db, source_root, target_root)



source_root = "/Volumes/Jerry_Disk/TCD-TIMIT/str/test/audio_gather/audio_ori"  # Original
target_root = "/Volumes/Jerry_Disk/TCD-TIMIT/str/test/audio_gather/audio_-20db"  # With Noise
snr_db = -20  # Set SNR

process_lrs3_test(source_root, target_root, snr_db)