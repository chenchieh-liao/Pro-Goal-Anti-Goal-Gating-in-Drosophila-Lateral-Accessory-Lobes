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
plt.figure(figsize=(10, 6))

for start_angle, input_map in grouped_data.items():
    sorted_inputs = sorted(input_map.keys())
    mean_diffs = [np.mean(input_map[x]) for x in sorted_inputs]
    std_diffs = [np.std(input_map[x]) for x in sorted_inputs]

    label = f"Start Angle: {start_angle}°"
    plt.errorbar(sorted_inputs, mean_diffs, yerr=std_diffs, fmt='-o', capsize=5, label=label)

plt.axhline(y=0, color='red', linewidth=2, linestyle='--')  # 或 linestyle='-' 變實線
# 圖表設定
plt.xlabel("LAL153 Input")
plt.ylabel("Angle Difference (°)")
plt.title("Mean Angle Difference vs LAL153 Input (Grouped by Start Angle)")
plt.legend(title="Start Angle")
plt.grid(False)
plt.tight_layout()
plt.savefig('AG_angle_diff_plot.png')

# 🧠 擬合 y=0 時的 LAL153 input for each start_angle
interpolated_data = []  # 用來儲存輸出資料 (start_angle, x_at_zero)

for start_angle, input_map in grouped_data.items():
    # 取得平均的曲線資料
    inputs = sorted(input_map.keys())
    mean_diffs = [np.mean(input_map[x]) for x in inputs]

    # 找出一對 y 值在 y=0 兩側的點
    found = False
    for i in range(1, len(inputs)):
        y1, y2 = mean_diffs[i - 1], mean_diffs[i]
        if y1 * y2 < 0:  # 一正一負
            x1, x2 = inputs[i - 1], inputs[i]
            # 線性內插求出 y=0 時的 x
            x_at_zero = x1 + (0 - y1) * (x2 - x1) / (y2 - y1)
            interpolated_data.append((start_angle, x_at_zero))
            found = True
            break
    if not found:
        print(f"⚠️ 沒有找到角度差穿越 y=0 的資料：start_angle = {start_angle}")

# 📝 輸出成 CSV 檔案
output_file = "angle_zero_fit.csv"
with open(output_file, "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Start_Angle", "LAL153_Input_at_Zero_Diff"])
    for start_angle, input_val in sorted(interpolated_data):
        writer.writerow([start_angle, input_val])

print(f"✅ 輸出完成：{output_file}")

# 讀取 CSV 檔
csv_file = "angle_zero_fit.csv"

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

# 📊 繪圖
plt.figure(figsize=(10, 6))
plt.plot(start_angles, inputs_at_zero, 'o-', color='teal')
plt.xlabel("Start Angle (°)")
plt.ylabel("LAL153 Input @ Angle Difference = 0")
plt.grid(False)
plt.tight_layout()
plt.savefig("AG_interpolated_x_plot.png")   