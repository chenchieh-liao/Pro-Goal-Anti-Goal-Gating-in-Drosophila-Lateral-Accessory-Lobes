import os
import numpy as np
import matplotlib.pyplot as plt

# 定義資料夾名稱及對應的 x 軸值
folders = ['data_ctr', 'data_no040', 'data_no121']
labels = ['Full model', '– DI1 ', '– DI2']  # 對應的標籤名稱
x_values = [10, 30, 60, 90]

# 初始化儲存平均值和標準差的字典
results = {folder: {'means': [], 'stds': []} for folder in folders}

# 讀取每個資料夾的檔案
for folder in folders:
    for x_val in x_values:
        file_means = []
        
            # 尋找 _1 到 _50 結尾的檔案
        for i in range(1, 51):
            filename = f"dna02_{x_val}_0.01_{i}.txt"
            file_path = os.path.join(folder, filename)
            
            if os.path.exists(file_path):
                # 讀取檔案的第 5000 到第 8000 行並提取第三欄數據
                with open(file_path, 'r') as f:
                    lines = f.readlines()[4999:8000]  # 提取第 5000 到第 8000 行（索引從 0 開始）
                    for line in lines:
                        columns = line.split()
                        if len(columns) >= 1:
                            third_column = float(columns[1])
                            file_means.append(third_column)

        # 計算該 x 值下所有檔案的平均值和標準差
        if file_means:
            mean_val = np.mean(file_means)
            std_val = np.std(file_means)
            results[folder]['means'].append(mean_val)
            results[folder]['stds'].append(std_val)
        else:
            # 如果沒有找到檔案，填充 NaN 保持長度一致
            results[folder]['means'].append(np.nan)
            results[folder]['stds'].append(np.nan)

# 繪圖
plt.figure(figsize=(15, 10))
for folder, label in zip(folders, labels):  # 同時迭代資料夾名稱與標籤
    means = results[folder]['means']
    stds = results[folder]['stds']
    if len(means) == len(x_values):  # 確認長度一致
        plt.errorbar(
            x_values, means, yerr=stds, label=label,
            capsize=10, capthick=3.5, elinewidth=3.5, linewidth=5  # 加粗線條與 error bar
        )
    else:
        print(f"Warning: {folder} does not have complete data. Skipping plot.")

plt.xlabel('Head-goal offset Δθ (°)', fontsize=30)
plt.ylabel('DNa02 firing rate difference', fontsize=30)
plt.xticks(fontsize = 25)
plt.yticks(fontsize = 25)
# plt.title('Lesion Test of Rare Stalemate', fontsize=30)
plt.legend(fontsize = 25)
plt.tick_params(width=3.5, length=8)

# 設置最外匡的粗度並移除上右匡線
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(5.5)
ax.spines['bottom'].set_linewidth(5.5)

ax.tick_params(width=4.5, length=12)

plt.savefig('fig2H_v3.svg', dpi=300)
plt.show()
