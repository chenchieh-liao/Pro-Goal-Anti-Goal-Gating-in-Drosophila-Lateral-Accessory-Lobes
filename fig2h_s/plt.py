import matplotlib.pyplot as plt
import os
# 定義檔案路徑
output_files_group1 = [
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig2e/data_ctr/dna02_30_0.01_DNa02.txt',
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig2e/data_ctr/dna02_30_0.01_LAL010.txt',
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig2e/data_ctr/dna02_30_0.01_LAL014.txt',
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig2e/data_ctr/dna02_30_0.01_LAL018.txt',
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig2e/data_ctr/dna02_30_0.01_LAL040.txt',
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig2e/data_ctr/dna02_30_0.01_LAL046.txt',
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig2e/data_ctr/dna02_30_0.01_LAL121.txt',
]

output_files_group2 = [
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig2e/data_no040/dna02_30_0.01_DNa02.txt',
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig2e/data_no040/dna02_30_0.01_LAL010.txt',
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig2e/data_no040/dna02_30_0.01_LAL014.txt',
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig2e/data_no040/dna02_30_0.01_LAL018.txt',
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig2e/data_no040/dna02_30_0.01_LAL040.txt',
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig2e/data_no040/dna02_30_0.01_LAL046.txt',
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig2e/data_no040/dna02_30_0.01_LAL121.txt',
]

output_files_group3 = [
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig2e/data_no121/dna02_30_0.01_DNa02.txt',
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig2e/data_no121/dna02_30_0.01_LAL010.txt',
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig2e/data_no121/dna02_30_0.01_LAL014.txt',
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig2e/data_no121/dna02_30_0.01_LAL018.txt',
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig2e/data_no121/dna02_30_0.01_LAL040.txt',
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig2e/data_no121/dna02_30_0.01_LAL046.txt',
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig2e/data_no121/dna02_30_0.01_LAL121.txt',
]

# 創建子圖
fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(13, 10), sharex=True, sharey=True)
axes = axes.flatten()

for ax, file1, file2, file3 in zip(axes, output_files_group1, output_files_group2, output_files_group3):
    # 讀取第一群資料
    x1, y1_1, y1_2 = [], [], []
    with open(file1, 'r') as f:
        for line in f:
            data = line.strip().split()
            x1.append(int(data[0]) / 10000)  # x 軸數值除以 10000
            y1_1.append(float(data[1]))
            y1_2.append(float(data[2]))

    # 讀取第二群資料
    x2, y2_1, y2_2 = [], [], []
    with open(file2, 'r') as f:
        for line in f:
            data = line.strip().split()
            x2.append(int(data[0]) / 10000)
            y2_1.append(float(data[1]))
            y2_2.append(float(data[2]))

    # 讀取第三群資料
    x3, y3_1, y3_2 = [], [], []
    with open(file3, 'r') as f:
        for line in f:
            data = line.strip().split()
            x3.append(int(data[0]) / 10000)
            y3_1.append(float(data[1]))
            y3_2.append(float(data[2]))

    # 繪圖
    ax.plot(x1, y1_1, label=f'{os.path.basename(file1)} - Col 2', color='blue')
    ax.plot(x1, y1_2, label=f'{os.path.basename(file1)} - Col 3', color='red')
    ax.plot(x2, y2_1, label=f'{os.path.basename(file2)} - Col 2', color='blue', linestyle='--')
    ax.plot(x2, y2_2, label=f'{os.path.basename(file2)} - Col 3', color='red', linestyle='--')
    ax.plot(x3, y3_1, label=f'{os.path.basename(file2)} - Col 2', color='blue', linestyle=':')
    ax.plot(x3, y3_2, label=f'{os.path.basename(file2)} - Col 3', color='red', linestyle=':')
    ax.set_title(os.path.basename(file1).replace('.txt', '').split('_', 3)[-1],fontsize = 16)
    ax.set_ylim(0, 1.0)
    #ax.legend(fontsize=8)

# 隱藏多餘的子圖
for i in range(len(output_files_group1), len(axes)):
    fig.delaxes(axes[i])

# 全局設定
fig.suptitle('Δθ = 30°', fontsize=18)
fig.text(0.5, 0.04, 'Time(s)', ha='center', fontsize=16)
fig.text(0.07, 0.5, 'Firing rate', va='center', rotation='vertical', fontsize=16)
#plt.tight_layout(rect=[0.03, 0.03, 1, 0.95])

plt.savefig('fig2e-30.png')