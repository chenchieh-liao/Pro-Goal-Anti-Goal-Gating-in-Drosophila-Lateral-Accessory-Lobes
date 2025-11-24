import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
import csv

# 📐 計算 0–360 度圓形座標下的角度差
def circular_diff(start, end):
    diff = (end - start) % 360
    return diff if diff <= 180 else diff-360

# 🔽 指定要處理的檔案們
file_list = [
    "full_model.txt"
]

# ⏬ 結構：{ start_angle: { LAL153_input: [angle_diffs] } }
grouped_data = defaultdict(lambda: defaultdict(list))

# 讀取資料
for file_path in file_list:
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) >= 6:
                try:
                    lal_input = float(parts[0].strip())
                    start_angle = float(parts[1].strip())
                    final_angle = float(parts[5].strip())

                    diff = circular_diff(start_angle, final_angle)

                    grouped_data[start_angle][lal_input].append(diff)
                except ValueError:
                    continue

# 📊 繪圖：每個 start_angle 一條線
plt.figure(figsize=(12, 8))

for start_angle, input_map in grouped_data.items():
    sorted_inputs = sorted(input_map.keys())
    mean_diffs = [np.mean(input_map[x]) for x in sorted_inputs]
    std_diffs = [np.std(input_map[x]) for x in sorted_inputs]

    label = f"{180-start_angle}°"
    plt.errorbar(sorted_inputs, mean_diffs, yerr=std_diffs, fmt='-o', capsize=5, label=label, linewidth=3.5)

plt.axhline(y=0, color='red', linewidth=4, linestyle='--')  # 或 linestyle='-' 變實線
# 圖表設定
plt.xlabel("Anti-goal Input", fontsize=20)
plt.xlim(0,30)
plt.ylabel(" Initial head-goal offset Δθ (°)",fontsize=20)
# plt.title("Mean Angle Difference vs LAL153 Input (Grouped by Start Angle)")
# plt.legend(title="Angle difference", fontsize=17)

ax = plt.gca()
ax.set_yticklabels(ax.get_yticks(), fontsize=17)
ax.tick_params(axis='y', labelcolor='teal', width=4, length=12)
ax.set_yticklabels(ax.get_yticks(), fontsize=17)

ax.tick_params(axis='x', width=4, length=12)
ax.set_xticklabels(ax.get_xticks(), fontsize=17)

for spine in ax.spines.values():
    spine.set_linewidth(4)

plt.grid(False)
plt.tight_layout()
plt.savefig('Fig5H.png',dpi = 300)