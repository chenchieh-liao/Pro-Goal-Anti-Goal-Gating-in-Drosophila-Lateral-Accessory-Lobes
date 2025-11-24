import matplotlib.pyplot as plt
import numpy as np

# 指定檔案與對應的 x 軸 label（要一一對應）
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

# 統一設定
font_size = 18
line_width = 3

# 收集各檔案的 reaction time 資料
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
                        continue  # 只處理 angle = 0 的資料
                except ValueError:
                    continue

                raw_reaction = parts[2].strip()
                try:
                    if raw_reaction in ['', 'None']:
                        reaction = 5  # 指定為 5 秒
                    else:
                        reaction = float(raw_reaction) / 10000  # 換成秒
                    reactions.append(reaction)
                except ValueError:
                    continue
    all_data.append(reactions)


# 繪製 boxplot
plt.figure(figsize=(14, 8))
box = plt.boxplot(all_data, patch_artist=True, widths=0.5)

# 美化每個 box
colors = plt.cm.Pastel1.colors
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_linewidth(line_width)

# 美化其他元素
for element in ['whiskers', 'caps', 'medians']:
    for line in box[element]:
        line.set_linewidth(line_width)

# x 軸設定
plt.xticks(np.arange(1, len(custom_xticks)+1), custom_xticks, fontsize=23, rotation=30, ha='center')

# y 軸設定
plt.ylabel("Reaction Time (s)", fontsize=25)
plt.yticks(fontsize=23)

# 邊框線條加粗
ax = plt.gca()
for spine in ax.spines.values():
    spine.set_linewidth(3)

plt.tight_layout()
plt.savefig('RS_reaction_time_boxplot_2.0.png', dpi=300)
plt.show()
