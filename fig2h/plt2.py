import matplotlib.pyplot as plt
import os

# 設定統一的線條和軸線粗度
line_width = 4  # 線條粗度
axis_width = 3  # 軸線粗度

# 定義檔案路徑
output_files_group1 = [
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig2h/data_ctr/dna02_30_0.01_DNa02.txt',
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig2h/data_ctr/dna02_30_0.01_LAL010.txt',
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig2h/data_ctr/dna02_30_0.01_LAL014.txt',
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig2h/data_ctr/dna02_30_0.01_LAL018.txt',
]

output_files_group2 = [
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig2h/data_no040/dna02_30_0.01_DNa02.txt',
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig2h/data_no040/dna02_30_0.01_LAL010.txt',
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig2h/data_no040/dna02_30_0.01_LAL014.txt',
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig2h/data_no040/dna02_30_0.01_LAL018.txt',
]

output_files_group3 = [
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig2h/data_no121/dna02_30_0.01_DNa02.txt',
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig2h/data_no121/dna02_30_0.01_LAL010.txt',
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig2h/data_no121/dna02_30_0.01_LAL014.txt',
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig2h/data_no121/dna02_30_0.01_LAL018.txt',
]

# 創建子圖，設定一行四個子圖
fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(15,5), sharey=False)
axes = axes.flatten()

for i, (ax, file1, file2, file3) in enumerate(zip(axes, output_files_group1, output_files_group2, output_files_group3)):
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

    # 讀取第三群資料
    x3, y3_1, y3_2 = [], [], []
    with open(file3, 'r') as f:
        for line in f:
            data = line.strip().split()
            x3.append(int(data[0]) / 10)
            y3_1.append(float(data[1]))
            y3_2.append(float(data[2]))

    # 繪圖
    ax.plot(x1, y1_1, label='Full model L', color='blue', linewidth=line_width)
    ax.plot(x1, y1_2, label='Full model R', color='red', linewidth=line_width)
    # ax.plot(x2, y2_1, label='No Exc. core 040 L', color='blue', linestyle='--', linewidth=line_width)
    # ax.plot(x2, y2_2, label='No Exc. core 040 R', color='red', linestyle='--', linewidth=line_width)
    ax.plot(x3, y3_1, label='- 121 output L', color='blue', linestyle=':', linewidth=line_width)
    ax.plot(x3, y3_2, label='- 121 output R', color='red', linestyle=':', linewidth=line_width)
    ax.set_title(os.path.basename(file1).replace('.txt', '').split('_', 3)[-1], fontsize=24)
    ax.set_ylim(0, 1.0)

    # 設定刻度與框線
    if i == 0:  # 最左邊的子圖保留完整 x, y 軸
        ax.set_ylabel('Firing rate', fontsize=22)
        ax.set_xlabel('Time (ms)', fontsize=22)
        ax.spines['left'].set_visible(True)
        ax.tick_params(axis='both', labelsize=16,width=3,length=7)
    else:  # 其他子圖隱藏 y 軸與 x 軸標籤
        ax.tick_params(labelleft=False, labelbottom=False,width=3,length=7)
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
fig.suptitle('Δθ = 30°', fontsize=30)
plt.tight_layout(rect=[0, 0.1, 1, 0.95])  # 調整子圖位置，留出更多空間給圖例

# 儲存圖片
plt.savefig('fig2h_v8_30.svg')

