import os
import numpy as np
import matplotlib.pyplot as plt

# 定義資料夾名稱及對應的 x 軸值
folders = ['data_ctr', 'data_Exc', 'data_hfExc']
labels = ['- Exc. core', '+ Exc. core ', '+ Exc. core (0.5)']  # 對應的標籤名稱
x_values = [-30, -60, -90 , -120, -150]
x_display_values = [abs(x) for x in x_values]  # 這是你希望在圖上看到的數字

# 初始化儲存平均值和標準差的字典
results = {folder: {'means': [], 'stds': []} for folder in folders}

# 讀取每個資料夾的檔案
for folder in folders:
    for x_val in x_values:
        file_means = []
        
            # 尋找 _1 到 _50 結尾的檔案
        for i in range(1, 51):
            filename = f"{x_val}_0.01_DNa02_{i}.txt"
            file_path = os.path.join(folder, filename)
            
            if os.path.exists(file_path):
                # 讀取檔案的第 5000 到第 8000 行並提取第三欄數據
                with open(file_path, 'r') as f:
                    lines = f.readlines()[3000:8000]  # 提取第 5000 到第 8000 行（索引從 0 開始）
                    for line in lines:
                        columns = line.split()
                        if len(columns) >= 3:
                            third_column = float(columns[2])
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
for folder, label in zip(folders, labels):
    means = results[folder]['means']
    stds = results[folder]['stds']
    if len(means) == len(x_values):
        plt.errorbar(
            x_display_values, means, yerr=stds, label=label,
            capsize=10, capthick=3.5, elinewidth=3.5, linewidth=5  # 加粗線條與 error bar
        )
    else:
        print(f"Warning: {folder} does not have complete data. Skipping plot.")

# 軸標籤與字體
plt.xlabel('Head-goal offset Δθ (°)', fontsize=30)
plt.ylabel('DNa02 firing rate', fontsize=30)
plt.yticks(fontsize=25)

# 設定 x 軸刻度與標籤（確保位置對應）
plt.xticks(
    ticks=x_display_values,
    labels=[str(val) for val in x_display_values],
    fontsize=25
)

# 軸線加粗
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(4)
ax.spines['bottom'].set_linewidth(4)

# 刻度線加粗
ax.tick_params(width=3.5, length=8)


plt.savefig('fig2E_v3.svg')
plt.show()
