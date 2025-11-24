import matplotlib.pyplot as plt
import os

# 設定統一的線條和軸線粗度
line_width = 4  # 線條粗度
axis_width = 3  # 軸線粗度

# 定義檔案路徑
output_files_group1 = [
   f'/home/chieh1102/FPLmodel/2025_fig5_v2/PG/dna02_90_0.01_LAL010.txt',
   f'/home/chieh1102/FPLmodel/2025_fig5_v2/PG/dna02_90_0.01_LAL014.txt',
   f'/home/chieh1102/FPLmodel/2025_fig5_v2/PG/dna02_90_0.01_LAL018.txt',
   f'/home/chieh1102/FPLmodel/2025_fig5_v2/PG/dna02_90_0.01_LAL153.txt',
   f'/home/chieh1102/FPLmodel/2025_fig5_v2/PG/dna02_90_0.01_LAL017.txt',
   f'/home/chieh1102/FPLmodel/2025_fig5_v2/PG/dna02_90_0.01_LAL040.txt',
   f'/home/chieh1102/FPLmodel/2025_fig5_v2/PG/dna02_90_0.01_LAL121.txt',
   f'/home/chieh1102/FPLmodel/2025_fig5_v2/PG/dna02_90_0.01_LAL126.txt',
   f'/home/chieh1102/FPLmodel/2025_fig5_v2/PG/dna02_90_0.01_LAL046.txt',
   f'/home/chieh1102/FPLmodel/2025_fig5_v2/PG/dna02_90_0.01_LAL073.txt',
   f'/home/chieh1102/FPLmodel/2025_fig5_v2/PG/dna02_90_0.01_LAL122.txt',
   f'/home/chieh1102/FPLmodel/2025_fig5_v2/PG/dna02_90_0.01_DNa01.txt',
   f'/home/chieh1102/FPLmodel/2025_fig5_v2/PG/dna02_90_0.01_DNa02.txt',
   f'/home/chieh1102/FPLmodel/2025_fig5_v2/PG/dna02_90_0.01_DNa03.txt',
   f'/home/chieh1102/FPLmodel/2025_fig5_v2/PG/dna02_90_0.01_DNa04.txt',
]


# output_files_group2 = [
#     f'/home/chieh1102/FPLmodel/open-loop_v5/fig2c/data_no1014/dna02_90_DNa02.txt',
#     f'/home/chieh1102/FPLmodel/open-loop_v5/fig2c/data_no1014/dna02_90_LAL014.txt',
#     f'/home/chieh1102/FPLmodel/open-loop_v5/fig2c/data_no1014/dna02_90_LAL018.txt',
#     f'/home/chieh1102/FPLmodel/open-loop_v5/fig2c/data_no1014/dna02_90_LAL040.txt',
#     f'/home/chieh1102/FPLmodel/open-loop_v5/fig2c/data_no1014/dna02_90_LAL121.txt',
# ]

# 創建子圖，設定一行五個子圖
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12, 10), sharey=False)
axes = axes.flatten()

for i, (ax, file1) in enumerate(zip(axes, output_files_group1)):
    # 讀取第一群資料
    x1, y1_1, y1_2 = [], [], []
    with open(file1, 'r') as f:
        for line in f:
            data = line.strip().split()
            x1.append(int(data[0])/10)
            y1_1.append(float(data[1]))
            y1_2.append(float(data[2]))

    # # 讀取第二群資料
    # x2, y2_1, y2_2 = [], [], []
    # with open(file2, 'r') as f:
    #     for line in f:
    #         data = line.strip().split()
    #         x2.append(int(data[0])/10)
    #         y2_1.append(float(data[1]))
    #         y2_2.append(float(data[2]))

    # 繪圖
    ax.plot(x1, y1_1, label='Full model L', color='blue', linewidth=line_width)
    ax.plot(x1, y1_2, label='Full model R', color='red', linewidth=line_width)
    # ax.plot(x2, y2_1, label='No Exc. core L', color='blue', linestyle='--', linewidth=line_width)
    # ax.plot(x2, y2_2, label='No Exc. core R', color='red', linestyle='--', linewidth=line_width)
    ax.set_title(os.path.basename(file1).replace('.txt', '').split('_', 3)[-1], fontsize=24)
    ax.set_ylim(0, 1.0)
    xticks = [0, 500, 1000, 1500]
    # 設定刻度與框線
    if i == 0 or i == 3:  # 最左邊的子圖保留完整 x, y 軸
        ax.set_ylabel('Firing rate', fontsize=22)
        ax.set_xlabel('Time (ms)', fontsize=22)
        ax.spines['left'].set_visible(True)
        ax.tick_params(axis='both', labelsize=16,width=3,length=7)
        ax.set_xticks(xticks)
    else:  # 其他子圖隱藏 y 軸與 x 軸標籤
        ax.tick_params(labelleft=False, labelbottom=False, width=3, length=7)
        ax.set_yticks([])
        ax.spines['left'].set_visible(False)

    # 移除所有子圖的框線
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # 調整軸線粗度
    for spine in ax.spines.values():
        spine.set_linewidth(axis_width)

# 在最右側新增圖例，並向右移動
handles, labels = ax.get_legend_handles_labels()
fig.legend(
    handles, 
    labels, 
    loc='center right', 
    fontsize=16, 
    frameon=False, 
    bbox_to_anchor=(0.99, 0.5)  # 調整圖例位置向右移
)

# 全局設定
fig.suptitle('Δθ = 90°', fontsize=30)
plt.tight_layout(rect=[0, 0.1, 0.85, 0.99])  # 調整子圖位置，留出更多空間給圖例

# 儲存圖片
plt.savefig('fig5b_2.svg')
plt.show()
