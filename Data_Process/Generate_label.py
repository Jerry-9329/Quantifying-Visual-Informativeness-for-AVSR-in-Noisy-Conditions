import os


lrs_root = "/Volumes/Jerry_Disk/LRS2/train_lrs2"
file_list_path = os.path.join(lrs_root, "file.list")
label_list_path = os.path.join(lrs_root, "label.list")

with open(file_list_path, "r") as fin, open(label_list_path, "w") as fout:
    for line in fin:
        clip_id = line.strip()
        if not clip_id:
            continue
        txt_path = os.path.join(lrs_root, clip_id + ".txt")

        if os.path.exists(txt_path):
            with open(txt_path, "r") as ftxt:
                lines = ftxt.readlines()
                text_line = next((l for l in lines if l.startswith("Text:")), None)
                if text_line:
                    text = text_line[len("Text:"):].strip()
                    fout.write(text + "\n")
                else:
                    print(f"⚠️ No Text line found in: {txt_path}")
                    fout.write("<missing_text>\n")
        else:
            print(f"⚠️ Text file not found: {txt_path}")
            fout.write("<missing_file>\n")

print(f"label.list saved to {label_list_path}")