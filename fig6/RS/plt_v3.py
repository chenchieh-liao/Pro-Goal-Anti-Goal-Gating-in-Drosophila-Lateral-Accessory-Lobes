import matplotlib.pyplot as plt
import numpy as np

# 檔案與 x 軸標籤
file_list = [
    "full_model.txt",
    "no121.txt",
    "noECC.txt",
    "noPFL2.txt",
    "noECC121.txt",
    "noECCpfl2.txt",
    "noPFL2121.txt",
]

custom_xticks = [
    'Full model',
    '– DI1/2',
    '– EC',
    '– PFL2',
    '– DI1/2, EC ',
    '– PFL2, EC',
    '– PFL2, DI1/2'
]

font_size = 18
line_width = 3

# 讀取資料
all_data = []
for file_path in file_list:
    reactions = []
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) >= 3:
                try:
                    angle = float(parts[1].strip())
                    if angle != 0:
                        continue  # 只處理 angle = 0
                except ValueError:
                    continue

                raw_reaction = parts[2].strip()
                try:
                    if raw_reaction in ['', 'None']:
                        reaction = 5
                    else:
                        reaction = float(raw_reaction) / 10000
                    reactions.append(reaction)
                except ValueError:
                    continue
    all_data.append(reactions)

# 判斷哪些組別全是 5 秒
is_all_5s = [all(np.isclose(r, 5)) for r in all_data]

# 為非全 5 秒的組別畫 boxplot
plt.figure(figsize=(14, 8))
box_positions = [i + 1 for i, flag in enumerate(is_all_5s) if not flag]
box_data = [data for data, flag in zip(all_data, is_all_5s) if not flag]

if box_data:
    box = plt.boxplot(box_data, patch_artist=True, widths=0.5, positions=box_positions)

    colors = plt.cm.Pastel1.colors
    for patch, color in zip(box['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_linewidth(line_width)

    for element in ['whiskers', 'caps', 'medians']:
        for line in box[element]:
            line.set_linewidth(line_width)

# 為全 5 秒的組別畫星號
# for i, flag in enumerate(is_all_5s, start=1):
#     if flag:
#         plt.scatter(i, 5, color='black', marker='*', s=400, zorder=3)

for i, flag in enumerate(is_all_5s, start=1):
    if flag:
        plt.text(i, 5, '*', fontsize=28, ha='center', va='center', color='black', zorder=3)


# x 軸設定
plt.xticks(np.arange(1, len(custom_xticks) + 1), custom_xticks, fontsize=23, rotation=30, ha='center')

# y 軸設定
plt.ylabel("Reaction Time (s)", fontsize=25)
plt.yticks(fontsize=23)

# 邊框線條加粗
ax = plt.gca()
for spine in ax.spines.values():
    spine.set_linewidth(3)

# 圖例說明
# plt.text(len(custom_xticks) - 1.5, 5.1, '*  All data = 5 s', fontsize=18, color='black')

plt.tight_layout()
plt.savefig('RS_reaction_time_2.0_v2.png', dpi=300)
plt.show()
