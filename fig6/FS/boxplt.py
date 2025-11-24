import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from collections import defaultdict
from scipy.stats import kruskal
import scikit_posthocs as sp
import itertools

# 設定樣式
sns.set(style="whitegrid")

file_list = [
    "full_model.txt",
    "no153.txt",
    "no122.txt",
    "no122153.txt",
    "no017.txt",
]

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

# Dunn test if significant
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
            # plt.plot([x1, x1, x2, x2], [y, y + step*0.2, y + step*0.2, y], lw=1.5, c='k')
            # plt.text((x1 + x2) / 2, y + step*0.25, "*", ha='center', va='bottom', color='red', fontsize=16)
            sig_idx += 1
else:
    print("→ No significant difference found.")

# 圖表設置
plt.title("Reaction Time Δθ = 0°")
plt.xlabel("File")
plt.ylabel("Reaction Time (s)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("reaction_time_boxplot_0_with_sig.png", dpi=300)
plt.show()
