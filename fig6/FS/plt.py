
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
import pandas as pd
from scipy.stats import kruskal
import seaborn as sns
import scikit_posthocs as sp
import itertools

# 指定要處理的 txt 檔案清單（加上路徑）
file_list = [
    "full_model.txt",
    "no017.txt",
    "no122.txt",
    "no153.txt"
]

# 開始繪圖
plt.figure(figsize=(10, 6))

for file_path in file_list:
    angle_rt_map = defaultdict(list)

    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) >= 3:
                try:
                    angle = float(parts[1].strip())
                    reaction = float(parts[2].strip())
                    adjusted_angle = 180 - angle
                    adjusted_reaction = reaction / 10000
                    angle_rt_map[adjusted_angle].append(adjusted_reaction)
                except ValueError:
                    continue

    # 計算每個角度的平均與標準差
    sorted_angles = sorted(angle_rt_map.keys())
    mean_rt = [np.mean(angle_rt_map[angle]) for angle in sorted_angles]
    std_rt = [np.std(angle_rt_map[angle]) for angle in sorted_angles]

    label = file_path.split("/")[-1]  # 顯示檔名作為圖例
    plt.errorbar(sorted_angles, mean_rt, yerr=std_rt, fmt='-o', capsize=4, label=label)

# 圖表設定
plt.xlabel("180 - Angle")
plt.ylabel("Reaction Time (s)")
plt.title("Average Reaction Time vs Adjusted Angle (Per File)")
plt.legend()
plt.grid(False)
plt.tight_layout()
plt.savefig('FS_reaction_time_plot.png', dpi=300)

# 收集資料
data = []
groups = []

for file_path in file_list:
    label = file_path.split("/")[-1]
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) >= 3:
                try:
                    angle = float(parts[1].strip())
                    reaction = float(parts[2].strip())
                    adjusted_angle = 180 - angle
                    adjusted_reaction = reaction / 10000
                    if abs(adjusted_angle - 0) < 1e-6:
                        data.append(adjusted_reaction)
                        groups.append(label)
                except ValueError:
                    continue

# 用 pandas 整理資料
df = pd.DataFrame({'Reaction Time': data, 'File': groups})
unique_labels = df['File'].unique()

# 畫圖
plt.figure(figsize=(10, 6))
ax = sns.boxplot(x='File', y='Reaction Time', data=df, showfliers=False, palette="Set2")
sns.stripplot(x='File', y='Reaction Time', data=df, color='black', jitter=True, alpha=0.6)

# Kruskal-Wallis test
print("\n== Kruskal-Wallis Test ==")
grouped_data = [df[df['File'] == label]['Reaction Time'].values for label in unique_labels]
stat, p = kruskal(*grouped_data)
print(f"Statistic = {stat:.4f}, p-value = {p:.4f}")

if p < 0.05:
    print("\n== Post Hoc Dunn Test (Holm-corrected) ==")
    posthoc = sp.posthoc_dunn(df, val_col='Reaction Time', group_col='File', p_adjust='holm')
    print(posthoc)

    # 繪製星號註記
    y_max = df['Reaction Time'].max()
    step = (y_max) * 0.1
    significance_level = 0.05
    sig_idx = 0

    # 逐對檢查是否顯著
    for i, j in itertools.combinations(range(len(unique_labels)), 2):
        val = posthoc.iloc[i, j]
        if val < significance_level:
            x1, x2 = i, j
            y = y_max + step * sig_idx
            plt.plot([x1, x1, x2, x2], [y, y + step*0.2, y + step*0.2, y], lw=1.5, c='k')
            plt.text((x1 + x2) / 2, y + step*0.25, "*", ha='center', va='bottom', color='red', fontsize=16)
            sig_idx += 1
else:
    print("→ No significant difference found.")
