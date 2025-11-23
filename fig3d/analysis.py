import os
import numpy as np
import csv

# 定義資料夾名稱及對應的 x 軸值
folders = ['data_ctr', 'data_noexcc', 'data_no121', 'data_noPFL2', 'data_noexcc_121', 'data_noexcc_pfl2', 'data_noPFL2_121']
labels = ['Full model', '— EC connection', '— LAL121', '— PFL2' ,'+ PFL2','+ 121','+ EC']  # 對應的標籤名稱
x_values = [0.07]

# 用來儲存最終的結果，每一列會是一筆資料
output_rows = [['Label', 'Noise Level', 'Abs(Col2 - Col3)', 'Col2 + Col3']]

# 開始處理每個資料夾與 noise level
for folder, label in zip(folders, labels):
    for x_val in x_values:
        x_val_strs = [f"{x_val:.2f}", f"{int(x_val)}"]
        file_abs_diffs = []
        file_sums = []

        for i in range(1, 51):
            for x_str in x_val_strs:
                filename = f"dna02_180_{x_str}_{i}.txt"
                file_path = os.path.join(folder, filename)

                if os.path.exists(file_path):
                    data = np.loadtxt(file_path)
                    if data.ndim == 1:
                        # 確保是二維的，即使只有一行
                        data = np.expand_dims(data, axis=0)
                    col2 = data[:, 1]
                    col3 = data[:, 2]
                    abs_diff = np.abs(col2 - col3)
                    sum_val = col2 + col3

                    file_abs_diffs.extend(abs_diff)
                    file_sums.extend(sum_val)

        if file_abs_diffs:
            mean_diff = np.mean(file_abs_diffs)
            mean_sum = np.mean(file_sums)
            output_rows.append([label, x_val, mean_diff, mean_sum])
        else:
            output_rows.append([label, x_val, 'NaN', 'NaN'])
            print(f"No files matched for x_val = {x_val} in folder {folder}")

# 將結果寫入 CSV 檔案
with open('diff&sum.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(output_rows)

print("CSV 輸出完成：diff&sum.csv")
