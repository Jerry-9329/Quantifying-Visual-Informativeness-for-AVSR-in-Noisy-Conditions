import os

lrs3_root = "/Volumes/Jerry_Disk/LRS2/train_lrs2"
output_file = os.path.join(lrs3_root, "file.list")

subset = "train"
target_dir = os.path.join(lrs3_root, subset)

with open(output_file, "w") as fout:
    for root, dirs, files in os.walk(target_dir):
        for f in files:
            if f.endswith(".mp4") and not f.startswith("._"):
                rel_path = os.path.relpath(os.path.join(root, f), lrs3_root)
                clip_id = os.path.splitext(rel_path)[0]
                fout.write(clip_id + "\n")

print(f"✅ file.list saved to {output_file}")