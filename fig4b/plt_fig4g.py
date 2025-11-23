import matplotlib.pyplot as plt
import os
import numpy as np
# 設定統一的線條和軸線粗度
line_width = 4  # 線條粗度
axis_width = 3  # 軸線粗度

# 取得當前程式所在資料夾
base_dir = os.path.dirname(os.path.abspath(__file__))

# 定義資料夾
data_ori_dir = os.path.join(base_dir, 'data_anti')
data_anti_dir = os.path.join(base_dir, 'data_nogoal')

# 定義檔案名稱（順序對應子圖）
filenames = [
    'dna02_90_0.01_DNa02.txt',
    'dna02_90_0.01_LAL010.txt',
    'dna02_90_0.01_LAL014.txt',
    'dna02_90_0.01_LAL018.txt',
    'dna02_90_0.01_LAL040.txt',
    'dna02_90_0.01_LAL122.txt',
    'dna02_90_0.01_LAL153.txt',
    'dna02_90_0.01_LAL017.txt'
]

# 拼出完整路徑
output_files_group1 = [os.path.join(data_ori_dir, f) for f in filenames]
output_files_group2 = [os.path.join(data_anti_dir, f) for f in filenames]

titles = ['DNa02', 'DE1', 'DE2', 'DE3', 'DI1', 'VI1', 'VE1', 'VE2']

import matplotlib.pyplot as plt
import os

fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(14, 8), sharey=False)
axes = axes.flatten()

for i, (ax, file1, file2) in enumerate(zip(axes, output_files_group1, output_files_group2)):
    # 讀取第一群資料
    x1, y1_1, y1_2 = [], [], []
    with open(file1, 'r') as f:
        for line in f:
            data = line.strip().split()
            x1.append(int(data[0]) / 10)
            y1_1.append(float(data[1]))
            y1_2.append(float(data[2]))

    # 讀取第二群資料
    x2, y2_1, y2_2 = [], [], []
    with open(file2, 'r') as f:
        for line in f:
            data = line.strip().split()
            x2.append(int(data[0]) / 10)
            y2_1.append(float(data[1]))
            y2_2.append(float(data[2]))

    # 繪圖
    ax.plot(x1, y1_1, label='+ goal input L', color='blue', alpha=0.3, linewidth=line_width)
    ax.plot(x1, y1_2, label='+ goal input R', color='red', alpha=0.3, linewidth=line_width)
    ax.plot(x2, y2_1, label='- goal input L', color='blue', linewidth=line_width)
    ax.plot(x2, y2_2, label='- goal input R', color='red', linewidth=line_width)

    # 設定標題
    ax.set_title(titles[i], fontsize=24)
    ax.set_ylim(0, 1.0)

    # 框線粗度設定
    for spine in ax.spines.values():
        spine.set_linewidth(axis_width)

    # 隱藏右上框線
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # 只顯示最左側子圖的 y 軸
    if i % 4 == 0:
        # ax.set_ylabel('Firing rate', fontsize=22)
        ax.spines['left'].set_visible(True)
        ax.tick_params(axis='y', labelsize=18, width=3, length=7)
    else:
        ax.set_yticks([])
        ax.tick_params(labelleft=False, width=3, length=7)
        ax.spines['left'].set_visible(False)

    xticks = np.arange(0, 801, 500) 
    # 只顯示最底排子圖的 x 軸
    if i == 4 :
        ax.set_xticks(xticks)
        ax.set_xlabel('Time (ms)', fontsize=22)
        ax.tick_params(axis='x', labelsize=18, width=3, length=7)
    elif i == 5 or i == 6 or i ==7:
        ax.set_xticks(xticks)
        ax.tick_params(axis='x', labelsize=18, width=3, length=7)
    else:
        ax.set_xticks(xticks)
        ax.tick_params(labelbottom=False, width=3, length=7)

# 特定子圖額外加上標籤（可視需要調整）
# axes[0].set_ylabel('firing rate', fontsize=22)
axes[4].set_ylabel('Firing rate', fontsize=25)
axes[4].set_xlabel('Time (ms)', fontsize=25)

# 取得圖例（用最後一個 ax）
handles, labels = ax.get_legend_handles_labels()
fig.legend(
    handles,
    labels,
    loc='center right',
    fontsize=16,
    frameon=False,
    bbox_to_anchor=(0.99, 0.5)
)

# 設定總標題
fig.suptitle('Δθ = 90°', fontsize=30)

# 調整 layout，右側空間保留給圖例
plt.tight_layout(rect=[0, 0.1, 0.85, 0.99])

# 儲存圖片
plt.savefig('fig4G.svg')

plt.show()
