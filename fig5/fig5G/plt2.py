import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
import os
import csv
from matplotlib.ticker import FuncFormatter

# 設定資料夾與要讀取的檔案清單
file_list = ["PFL3+PFL2_firing_rate_change_goal.txt"]
csv_file = "angle_zero_fit.csv"

# 初始化圖形與雙 y 軸
fig, ax1 = plt.subplots(figsize=(10, 8))
ax2 = ax1.twinx()
# ---------- 第一組資料畫在 ax1 ----------
for file in sorted(file_list):
    data = []
    data2 = []
    print(f"Processing file: {file}")
    with open(file, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) == 4:
                key = int(parts[0])
                val1 = float(parts[1])
                val2 = float(parts[2])
                val3 = float(parts[3])
                diff = abs(val2 - val1)
                total = val3 * 0.3 + diff
                data.append((key, total))
                data2.append((key, diff))

    grouped = defaultdict(list)
    grouped2 = defaultdict(list)
    for key, total in data:
        grouped[key].append(total)
    for key, diff in data2:
        grouped2[key].append(diff)

    x_vals, means, stds = [], [], []
    x_vals2, means2, stds2 = [], [], []
    for key in sorted(grouped.keys()):
        totals = grouped[key]
        x_vals.append(180 - key)
        means.append(np.mean(totals))
        stds.append(np.std(totals))

    for key in sorted(grouped2.keys()):
        diffs = grouped2[key]
        x_vals2.append(180 - key)
        means2.append(np.mean(diffs))
        stds2.append(np.std(diffs))

    # ax1.errorbar(x_vals, means, yerr=stds, fmt='-', capsize=3, label='PFL2+3', color='red', linewidth=4)
    ax2.errorbar(x_vals2, means2, yerr=stds2, fmt='-', capsize=3, label='PFL3', color='red', linewidth=4)
    ax2.set_ylabel('Pro-goal input strength (PFL3)', fontsize=20, color='red')
    ax2.tick_params(axis='y', labelcolor='red', width=4, length=12)
    ax2.set_yticklabels(ax1.get_yticks(), fontsize=17)
    ax2.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y:.2f}'))  # 控制小數點位數

# ---------- 第二組資料畫在 ax2 ----------


start_angles = []
inputs_at_zero = []
with open(csv_file, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            start_angle = float(row["Start_Angle"])
            input_val = float(row["LAL153_Input_at_Zero_Diff"])
            start_angles.append(start_angle)
            inputs_at_zero.append(input_val)
        except ValueError:
            continue

ax1.plot(start_angles, inputs_at_zero, 'o-', color='blue', label='Anti-goal Input',linewidth=4)
ax1.set_ylabel('Anti-goal input threshold', fontsize=20, color='blue')
ax1.tick_params(axis='y', labelcolor='teal', width=4, length=12)
ax1.set_yticklabels(ax2.get_yticks(), fontsize=17)
ax1.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y:.2f}'))  # 控制小數點位數


# ---------- x 軸設定 ----------
ax1.set_xlabel('Initial head-goal offset Δθ (°)', fontsize=20)
ax1.tick_params(axis='x', width=4, length=12)
ax1.set_xticklabels(ax1.get_xticks(), fontsize=17)

# ---------- 圖例 ----------
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
# plt.legend(lines1 + lines2, labels1 + labels2, loc='upper right', fontsize=15)

# ---------- 邊框粗度 ----------
for spine in ax1.spines.values():
    spine.set_linewidth(4)
for spine in ax2.spines.values():
    spine.set_linewidth(4)

plt.tight_layout()
plt.savefig("Fig5I.png", dpi=300)

