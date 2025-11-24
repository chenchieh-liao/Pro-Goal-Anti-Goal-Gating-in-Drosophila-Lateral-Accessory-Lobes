import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
import os

file_list = [
    "full_model.txt",
    "no121.txt",
    "noECC.txt",
    "noPFL2.txt",
    "noECC121.txt",
    "noECCpfl2.txt",
    "noPFL2121.txt",
]

# 為每個檔案產生一張獨立的直方圖
for file_path in file_list:
    adjusted_reactions = []

    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) >= 3:
                try:
                    angle = float(parts[1].strip())
                    reaction = float(parts[2].strip())
                    adjusted_reaction = reaction / 10000
                    adjusted_reactions.append(adjusted_reaction)
                except ValueError:
                    continue

    # 畫圖
    plt.figure(figsize=(8, 5))
    plt.hist(adjusted_reactions, bins=30, color='skyblue', edgecolor='black', alpha=0.8)
    plt.xlabel("Adjusted Reaction Time (s)")
    plt.ylabel("Count")
    plt.title(f"Distribution of Adjusted Reaction Time\n{file_path}")
    plt.tight_layout()

    # 儲存檔案
    output_name = f"/home/ubuntu/2025_0424_fig6_v2/RS/distribution/{os.path.splitext(file_path)[0]}_reaction_dist.png"
    plt.savefig(output_name, dpi=300)
    plt.close()
