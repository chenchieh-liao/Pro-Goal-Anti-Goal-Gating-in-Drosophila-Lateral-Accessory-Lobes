import os
import numpy as np
import matplotlib.pyplot as plt

# 定義資料夾名稱及對應的 x 軸值
folders = ['data_ctr', 'data_noexcc', 'data_no040', 'data_no121','data_no040121', 'data_noPFL2', 'data_noexcc_121', 'data_noexcc_pfl2', 'data_noPFL2_121']
labels = ['Full model', '— EC connection', '— LAL040', '— LAL121', '- LAL040 & 121', '— PFL2' ,'+ PFL2','+ 121','+ EC']  # 對應的標籤名稱
x_values = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]

# 初始化儲存平均值和標準差的字典
results = {folder: {'means': [], 'stds': []} for folder in folders}

# 讀取每個資料夾的檔案
for folder in folders:
    for x_val in x_values:
        file_means = []
        
        # 將 x_val 標準化為可能的字串格式
        x_val_strs = [f"{x_val:.2f}", f"{int(x_val)}"]  # 允許小數及整數格式
        matched_files = []

        # 尋找所有符合條件的檔案
        for i in range(1, 51):
            for x_str in x_val_strs:
                filename = f"dna02_180_{x_str}_{i}.txt"
                file_path = os.path.join(folder, filename)
                if os.path.exists(file_path):
                    matched_files.append(file_path)

                    # 讀取檔案數據並計算第二欄與第三欄的絕對差值平均
                    data = np.loadtxt(file_path)
                    abs_diff = np.abs(data[:, 1] - data[:, 2])
                    file_means.append(np.mean(abs_diff))
        
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

        # 偵錯用：列出所有找到的檔案
        if not matched_files:
            print(f"No files matched for x_val = {x_val} in folder {folder}")

# 繪圖
plt.figure(figsize=(12, 8))
for folder, label in zip(folders, labels):  # 同時迭代資料夾名稱與標籤
    means = results[folder]['means']
    stds = results[folder]['stds']
    if len(means) == len(x_values):  # 確認長度一致
        plt.errorbar(x_values, means, yerr=stds, label=label, capsize=3, linewidth=4)
    else:
        print(f"Warning: {folder} does not have complete data. Skipping plot.")

# 設定軸與圖標題
plt.xlabel('Noise level', fontsize=25)
plt.ylabel('Abs DNa02 firing rate difference', fontsize=25)
plt.title('Lesion test of rare stalemate', fontsize=35)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=25)

# 儲存圖檔
plt.savefig('fig3E_v3.png', bbox_inches='tight')
plt.show()
