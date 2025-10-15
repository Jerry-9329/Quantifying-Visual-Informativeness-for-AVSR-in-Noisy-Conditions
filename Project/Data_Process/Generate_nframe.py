import os

lrs3_root = "/Volumes/Jerry_Disk/LRS2/train_lrs2"
file_list = os.path.join(lrs3_root, "file.list")
label_list = os.path.join(lrs3_root, "label.list")
nframes_audio_file = os.path.join(lrs3_root, "nframes.audio.0")
nframes_video_file = os.path.join(lrs3_root, "nframes.video.0")

output_dir = os.path.join(lrs3_root, "decode_data")
os.makedirs(output_dir, exist_ok=True)

fids = [x.strip() for x in open(file_list)]
labels = [x.strip().lower() for x in open(label_list)]
nfa = [x.strip() for x in open(nframes_audio_file)]
nfv = [x.strip() for x in open(nframes_video_file)]

# For test.tsv
with open(os.path.join(output_dir, "test.tsv"), "w") as ft:
    ft.write("/\n")
    for fid, a, v in zip(fids, nfa, nfv):
        video_path = os.path.abspath(os.path.join(lrs3_root, "video", fid + ".mp4"))
        audio_path = os.path.abspath(os.path.join(lrs3_root, "audio", fid + ".wav"))
        ft.write(f"{fid}\t{video_path}\t{audio_path}\t{v}\t{a}\n")

# For test.wrd
with open(os.path.join(output_dir, "test.wrd"), "w") as fw:
    for lbl in labels:
        fw.write(lbl + "\n")