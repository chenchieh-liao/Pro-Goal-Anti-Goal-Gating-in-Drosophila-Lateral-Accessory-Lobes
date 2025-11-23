import os
import numpy as np
import matplotlib.pyplot as plt

# 定義資料夾名稱及對應的 x 軸值
folders = ['data_ctr', 'data_noexcc', 'data_no040','data_no121','data_no121', 'data_noPFL2', 'data_noexcc_121', 'data_noexcc_pfl2', 'data_noPFL2_121']
labels = ['Full model', '— EC connection', '— LAL040', '— LAL121', '— LAL040 & 121', '— PFL2' ,'+ PFL2','+ LAL121','+ EC connection']  # 對應的標籤名稱
x_values = [ 0.00,0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]

# 初始化儲存平均值和標準差的字典
results = {folder: {'means': [], 'stds': []} for folder in folders}


# 讀取每個資料夾的檔案
for folder in folders:
    for x_val in x_values:
        file_means = []
        
        # 尋找 _1 到 _50 結尾的檔案
        for i in range(1, 51):
            filename = f"dna02_180_{x_val:.2f}_{i}.txt"
            file_path = os.path.join(folder, filename)
            
            if os.path.exists(file_path):
                data = np.loadtxt(file_path)
                abs_data = np.abs(data)
                file_means.append(np.mean(abs_data))
            else:
                print(f"File not found: {file_path}")
        
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
            mean_val = np.nan
            std_val = np.nan
            print(f"No valid data for x_val: {x_val} in folder: {folder}")

# 設定參數
axis_label_size = 25
axis_title_size = 30
plot_title_size = 35
line_width = 3  # XY軸線條寬度
cap_size = 3    # 誤差棒端點大小
line_thickness = 4  # 資料線條寬度

# # 繪圖前檢查資料長度與內容
# for folder, label in zip(folders, labels):
#     means = results[folder]['means']
#     stds = results[folder]['stds']
#     print(f"Plotting {folder} - Means: {means}, Stds: {stds}")
#     if len(means) == len(x_values):
#         plt.errorbar(x_values, means, yerr=stds, label=label, capsize=cap_size, linewidth=line_thickness)
#     else:
#         print(f"Skipping {folder}: Data length mismatch.")

# # 繪圖
plt.figure(figsize=(12, 8))
for folder, label in zip(folders, labels):  # 同時迭代資料夾名稱與標籤
    means = results[folder]['means']
    stds = results[folder]['stds']
    if len(means) == len(x_values):  # 確認長度一致
        plt.errorbar(x_values, means, yerr=stds, label=label, capsize=cap_size, linewidth=line_thickness)
    else:
        print(f"Warning: {folder} does not have complete data. Skipping plot.")

# 設定軸與圖標題
plt.xlabel('Noise level', fontsize=axis_label_size)
plt.ylabel('Abs DNa02 firing rate difference', fontsize=axis_label_size)
plt.title('Lesion test of rare stalemate', fontsize=plot_title_size)

# 調整圖例位置及外觀
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=axis_label_size)

# 去掉上與右邊框線
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# 加粗XY軸
plt.gca().spines['bottom'].set_linewidth(line_width)
plt.gca().spines['left'].set_linewidth(line_width)

# 調整XY軸刻度字體大小
plt.tick_params(axis='x', labelsize=axis_label_size)
plt.tick_params(axis='y', labelsize=axis_label_size)

# 儲存圖檔
plt.savefig('fig3E_v3.png', bbox_inches='tight')
plt.show()
