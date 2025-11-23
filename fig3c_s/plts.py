import matplotlib.pyplot as plt
import os
import numpy as np

line_width = 4
axis_width = 3

# 檔案群組 (共 15 個檔案，這裡只放例子，你要把全部路徑放進去)
output_files_group1 = [
    '/home/chieh1102/FPLmodel/open-loop_v5/fig3c_s/data_ctr/dna02_180_0.01_LAL010.txt',
    '/home/chieh1102/FPLmodel/open-loop_v5/fig3c_s/data_ctr/dna02_180_0.01_LAL014.txt',
    '/home/chieh1102/FPLmodel/open-loop_v5/fig3c_s/data_ctr/dna02_180_0.01_LAL018.txt',
    '/home/chieh1102/FPLmodel/open-loop_v5/fig3c_s/data_ctr/dna02_180_0.01_LAL153.txt',
    '/home/chieh1102/FPLmodel/open-loop_v5/fig3c_s/data_ctr/dna02_180_0.01_LAL017.txt',
    '/home/chieh1102/FPLmodel/open-loop_v5/fig3c_s/data_ctr/dna02_180_0.01_LAL040.txt',
    '/home/chieh1102/FPLmodel/open-loop_v5/fig3c_s/data_ctr/dna02_180_0.01_LAL121.txt',
    '/home/chieh1102/FPLmodel/open-loop_v5/fig3c_s/data_ctr/dna02_180_0.01_LAL126.txt',
    '/home/chieh1102/FPLmodel/open-loop_v5/fig3c_s/data_ctr/dna02_180_0.01_LAL073.txt',
    '/home/chieh1102/FPLmodel/open-loop_v5/fig3c_s/data_ctr/dna02_180_0.01_LAL122.txt',
    '/home/chieh1102/FPLmodel/open-loop_v5/fig3c_s/data_ctr/dna02_180_0.01_LAL046.txt',
    '/home/chieh1102/FPLmodel/open-loop_v5/fig3c_s/data_ctr/dna02_180_0.01_DNa01.txt',
    '/home/chieh1102/FPLmodel/open-loop_v5/fig3c_s/data_ctr/dna02_180_0.01_DNa02.txt',
    '/home/chieh1102/FPLmodel/open-loop_v5/fig3c_s/data_ctr/dna02_180_0.01_DNa03.txt',
    '/home/chieh1102/FPLmodel/open-loop_v5/fig3c_s/data_ctr/dna02_180_0.01_DNa04.txt',

]
output_files_group2 = [
    '/home/chieh1102/FPLmodel/open-loop_v5/fig3c_s/data_ctr/dna02_180_0.07_LAL010.txt',
    '/home/chieh1102/FPLmodel/open-loop_v5/fig3c_s/data_ctr/dna02_180_0.07_LAL014.txt',
    '/home/chieh1102/FPLmodel/open-loop_v5/fig3c_s/data_ctr/dna02_180_0.07_LAL018.txt',
    '/home/chieh1102/FPLmodel/open-loop_v5/fig3c_s/data_ctr/dna02_180_0.07_LAL153.txt',
    '/home/chieh1102/FPLmodel/open-loop_v5/fig3c_s/data_ctr/dna02_180_0.07_LAL017.txt',
    '/home/chieh1102/FPLmodel/open-loop_v5/fig3c_s/data_ctr/dna02_180_0.07_LAL040.txt',
    '/home/chieh1102/FPLmodel/open-loop_v5/fig3c_s/data_ctr/dna02_180_0.07_LAL121.txt',
    '/home/chieh1102/FPLmodel/open-loop_v5/fig3c_s/data_ctr/dna02_180_0.07_LAL126.txt',
    '/home/chieh1102/FPLmodel/open-loop_v5/fig3c_s/data_ctr/dna02_180_0.07_LAL073.txt',
    '/home/chieh1102/FPLmodel/open-loop_v5/fig3c_s/data_ctr/dna02_180_0.07_LAL122.txt',
    '/home/chieh1102/FPLmodel/open-loop_v5/fig3c_s/data_ctr/dna02_180_0.07_LAL046.txt',
    '/home/chieh1102/FPLmodel/open-loop_v5/fig3c_s/data_ctr/dna02_180_0.07_DNa01.txt',
    '/home/chieh1102/FPLmodel/open-loop_v5/fig3c_s/data_ctr/dna02_180_0.07_DNa02.txt',
    '/home/chieh1102/FPLmodel/open-loop_v5/fig3c_s/data_ctr/dna02_180_0.07_DNa03.txt',
    '/home/chieh1102/FPLmodel/open-loop_v5/fig3c_s/data_ctr/dna02_180_0.07_DNa04.txt',
]

titles = [
    "DE1", "DE2", "DE3", "VE1", "VE2",
    "DI1", "DI2", "DI3", "DI4", "VI1",
    "VI2", "DNa01", "DNa02", "DNa03", "DNa04"
]

# 創建 3x5 子圖
fig, axes = plt.subplots(3, 5, figsize=(12, 12), sharex=False, sharey=True, dpi=1800)
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
    ax.plot(x1, y1_1, color='blue', linewidth=line_width, label='noise 0.01 L')
    ax.plot(x1, y1_2, color='red', linewidth=line_width, label='noise 0.01 R')
    ax.plot(x2, y2_1, color='blue', linestyle='--', linewidth=line_width, alpha=0.3, label='noise 0.07 L')
    ax.plot(x2, y2_2, color='red', linestyle='--', linewidth=line_width, alpha=0.3, label='noise 0.07 R')

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
fig.suptitle('Δθ = 180°', fontsize=28)

# 圖例放右上
handles, labels = axes[0].get_legend_handles_labels()
fig.legend(
    handles, labels,
    loc='upper right',
    bbox_to_anchor=(0.9, 0.85),
    fontsize=18,
    frameon=False
)


plt.savefig('fig3C_s.png')
plt.show()
