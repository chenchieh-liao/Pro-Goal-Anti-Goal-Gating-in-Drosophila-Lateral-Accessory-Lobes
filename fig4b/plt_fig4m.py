import matplotlib.pyplot as plt
import os
import numpy as np
# 設定統一的線條和軸線粗度
line_width = 4  # 線條粗度
axis_width = 3  # 軸線粗度

# 取得程式所在資料夾
base_dir = os.path.dirname(os.path.abspath(__file__))

# 資料夾
data_dir = os.path.join(base_dir, 'data_Front')

# 檔案名稱
filenames_group1 = [
    'dna02_0_0.01_DNa02.txt',
    'dna02_0_0.01_LAL014.txt',
    'dna02_0_0.01_LAL122.txt',
    'dna02_0_0.01_LAL153.txt',
]

filenames_group2 = [
    'dna02_0_0.07_DNa02.txt',
    'dna02_0_0.07_LAL014.txt',
    'dna02_0_0.07_LAL122.txt',
    'dna02_0_0.07_LAL153.txt',
]

# 拼出完整路徑
output_files_group1 = [os.path.join(data_dir, f) for f in filenames_group1]
output_files_group2 = [os.path.join(data_dir, f) for f in filenames_group2]

# 自訂子圖標題（順序對應檔案）
titles = ['DNa02', 'DE2', 'VI1', 'VE1']

import matplotlib.pyplot as plt
import os

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(6, 8), sharey=False)
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
    ax.plot(x1, y1_1, label='noise = 0.01 L', color='blue',  linewidth=line_width)
    ax.plot(x1, y1_2, label='noise = 0.01 R', color='red',  linewidth=line_width)
    ax.plot(x2, y2_1, label='noise = 0.07 L', color='blue', alpha=0.3, linewidth=line_width)
    ax.plot(x2, y2_2, label='noise = 0.07 R', color='red', alpha=0.3, linewidth=line_width)

    # 設定標題
    ax.set_title(os.path.basename(file1).replace('.txt', '').split('_', 3)[-1], fontsize=24)
    ax.set_ylim(0, 1.0)

    # 框線粗度設定
    for spine in ax.spines.values():
        spine.set_linewidth(axis_width)

    # 隱藏右上框線
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

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
    if i % 2 == 0:
        # ax.set_ylabel('Firing rate', fontsize=22)
        ax.spines['left'].set_visible(True)
        ax.tick_params(axis='y', labelsize=18, width=3, length=7)
    else:
        ax.set_yticks([])
        ax.tick_params(labelleft=False, width=3, length=7)
        ax.spines['left'].set_visible(False)

    xticks = np.arange(0, 801, 500) 
    # 只顯示最底排子圖的 x 軸
    if i == 2 :
        ax.set_xticks(xticks)
        ax.set_xlabel('Time (ms)', fontsize=22)
        ax.tick_params(axis='x', labelsize=18, width=3, length=7)
    elif i == 3 :
        ax.set_xticks(xticks)
        ax.tick_params(axis='x', labelsize=18, width=3, length=7)
    else:
        ax.set_xticks(xticks)
        ax.tick_params(labelbottom=False, width=3, length=7)

# 特定子圖額外加上標籤（可視需要調整）
# axes[0].set_ylabel('firing rate', fontsize=22
axes[2].set_ylabel('Firing rate', fontsize=25)
axes[2].set_xlabel('Time (ms)', fontsize=25)

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
fig.suptitle('Δθ = 0°', fontsize=30)

# 調整 layout，右側空間保留給圖例
plt.tight_layout()

# 儲存圖片
plt.savefig('fig4M.svg')

plt.show()
