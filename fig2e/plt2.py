import os
import numpy as np
import matplotlib.pyplot as plt

# 定義資料夾名稱及對應的 x 軸值
folders = ['data_ctr', 'data_Exc', 'data_hfExc']
labels = ['- Exc. core', '+ Exc. core ', '+ Exc. core (0.5)']  # 對應的標籤名稱
x_values = [0,-30, -60, -90]

# 初始化儲存平均值和標準差的字典
results = {folder: {'means': [], 'stds': [], 'raw_data': []} for folder in folders}

# 讀取每個資料夾的檔案
for folder in folders:
    for x_val in x_values:
        file_data = []
        
        # 尋找 _1 到 _50 結尾的檔案
        for i in range(1, 51):
            filename = f"{x_val}_0.01_DNa02_{i}.txt"
            file_path = os.path.join(folder, filename)
            
            if os.path.exists(file_path):
                # 讀取檔案的第 5000 到第 8000 行並提取第三欄數據
                with open(file_path, 'r') as f:
                    lines = f.readlines()[4999:8000]  # 提取第 5000 到第 8000 行（索引從 0 開始）
                    for line in lines:
                        columns = line.split()
                        if len(columns) >= 3:
                            third_column = float(columns[2])
                            file_data.append(third_column)

        # 保存原始數據
        results[folder]['raw_data'].append(file_data)

# 計算三個 folder 裡的所有最大值
all_values = []
for folder in folders:
    for data in results[folder]['raw_data']:
        if data:
            all_values.extend(data)

# 找出整體最大值
global_max = max(all_values) if all_values else 1  # 避免全空

# 使用最大值正規化並計算均值和標準差
for folder in folders:
    for data in results[folder]['raw_data']:
        if data:
            if global_max != 0:
                normalized_data = [value / global_max for value in data]
            else:
                normalized_data = [0 for _ in data]  # 避免除以 0

            mean_val = np.mean(normalized_data)
            std_val = np.std(normalized_data)

            results[folder]['means'].append(mean_val)
            results[folder]['stds'].append(std_val)
        else:
            results[folder]['means'].append(np.nan)
            results[folder]['stds'].append(np.nan)

# 繪圖
plt.figure(figsize=(15, 10))
for folder, label in zip(folders, labels):  # 同時迭代資料夾名稱與標籤
    means = results[folder]['means']
    stds = results[folder]['stds']
    if len(means) == len(x_values):  # 確認長度一致
        plt.errorbar(x_values, means, yerr=stds, label=label, capsize=5, linewidth=6, elinewidth=4)
    else:
        print(f"Warning: {folder} does not have complete data. Skipping plot.")

plt.xlabel('angle difference', fontsize=30)
plt.ylabel('Firing Rate (Normalized)', fontsize=30) 
plt.xticks(fontsize = 25)
plt.yticks(fontsize = 25)
# plt.title('Lesion Test of Rare Stalemate (Normalized)', fontsize=30)
plt.legend(fontsize=25)

# 設置最外匡的粗度並移除上右匡線
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_linewidth(4)
plt.gca().spines['bottom'].set_linewidth(4)

plt.savefig('fig2E_normalized.png')
plt.show()
