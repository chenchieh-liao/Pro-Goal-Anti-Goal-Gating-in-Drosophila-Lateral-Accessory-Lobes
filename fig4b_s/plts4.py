import matplotlib.pyplot as plt
import os
import numpy as np

line_width = 4
axis_width = 3

# 取得當前程式所在資料夾
base_dir = os.path.dirname(os.path.abspath(__file__))

# 定義資料夾
data_ori_dir = os.path.join(base_dir, 'data_017_0.6')
data_anti_dir = os.path.join(base_dir, 'data_anti')

# 定義檔案名稱（順序對應子圖）
filenames = [
    'dna02_90_0.01_LAL010.txt',
    'dna02_90_0.01_LAL014.txt',
    'dna02_90_0.01_LAL018.txt',
    'dna02_90_0.01_LAL153.txt',
    'dna02_90_0.01_LAL017.txt',
    'dna02_90_0.01_LAL040.txt',
    'dna02_90_0.01_LAL121.txt',
    'dna02_90_0.01_LAL126.txt',
    'dna02_90_0.01_LAL073.txt',
    'dna02_90_0.01_LAL122.txt',
    'dna02_90_0.01_LAL046.txt',
    'dna02_90_0.01_DNa01.txt',
    'dna02_90_0.01_DNa02.txt',
    'dna02_90_0.01_DNa03.txt',
    'dna02_90_0.01_DNa04.txt', 
]

# 拼出完整路徑
output_files_group1 = [os.path.join(data_ori_dir, f) for f in filenames]
output_files_group2 = [os.path.join(data_anti_dir, f) for f in filenames]

titles = [
    "DE1", "DE2", "DE3", "VE1", "VE2",
    "DI1", "DI2", "DI3", "DI4", "VI1",
    "VI2", "DNa01", "DNa02", "DNa03", "DNa04"
]

# 創建 3x5 子圖
fig, axes = plt.subplots(3, 5, figsize=(12, 14), sharex=False, sharey=True, dpi=1800)
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
    ax.plot(x1, y1_1, color='blue', linewidth=line_width, label='L strengthen VE2')
    ax.plot(x1, y1_2, color='red', linewidth=line_width, label='R strengthen VE2')
    ax.plot(x2, y2_1, color='blue', linewidth=line_width, alpha=0.3, label='L Full model')
    ax.plot(x2, y2_2, color='red', linewidth=line_width, alpha=0.3, label='R Full model')

    ax.set_title(titles[i], fontsize=20)
    ax.set_ylim(0, 1.0)
    ax.set_xticks([0, 500])


    # 左邊第一列
    if i % 5 == 0:
        ax.tick_params(axis='y', which='both', labelsize=16, labelleft=True)
    else:
        ax.tick_params(axis='y', which='both', left=False, labelleft=False)
        ax.spines['left'].set_visible(False)

    # 最下面一行保留 x label
    if i // 5 != 2:
        ax.tick_params(labelbottom=False)

    if i == 5:
        ax.set_ylabel('Firing rate', fontsize=22)

    if i == 12:
        ax.set_xlabel('Time (ms)', fontsize=22)

    # 移除不必要的邊框
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    for spine in ax.spines.values():
        spine.set_linewidth(axis_width)

    ax.tick_params(axis='both', labelsize=16, width=3, length=7)

# 全局標題
fig.suptitle('Δθ = 90°', fontsize=28)

# 圖例放右上
handles, labels = axes[0].get_legend_handles_labels()
fig.legend(
    handles, labels,
    loc='upper right',
    bbox_to_anchor=(0.95, 1.00),
    fontsize=18,
    frameon=False
)

plt.tight_layout(rect=[0, 0, 1, 0.88])

plt.savefig('fig4F_s.png',dpi= 90)
plt.show()
