import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def load_csv_data(file_list):
    # 初始化一個字典來存儲各 CSV 檔案的資料
    data_dict = {}

    for file in file_list:
        # 讀取 CSV
        df = pd.read_csv(file)
        # 以 Filename 為索引，並取得 Average Angular Velocity
        data_dict[file] = df.set_index('Filename')['Average Angular Velocity (°/s)']

    return data_dict

def create_heatmap(data_dict):
    # 確保所有 CSV 檔案的 Filename 是對齊的，並填補缺失值
    all_filenames = list(set.intersection(*[set(data.index) for data in data_dict.values()]))
    
    # 創建一個空的 DataFrame，用於存儲熱圖的數據
    heatmap_data = pd.DataFrame(index=all_filenames, columns=data_dict.keys())

        
    # 填充熱圖數據
    for file, data in data_dict.items():
        for filename in all_filenames:
            if filename in data.index:
                heatmap_data.at[filename, file] = data[filename]
            else:
                heatmap_data.at[filename, file] = np.nan

    # 檢查 y_order 中的元素是否都存在於 heatmap_data 中
    valid_y_order = [filename for filename in y_order if filename in heatmap_data.index]
    
    # 使用有效的 y_order 重新排序
    heatmap_data = heatmap_data.reindex(valid_y_order)

    # 填補 NaN 值，這裡我們用 0 或者其他值來填充 NaN
    heatmap_data = heatmap_data.fillna(0)  # 或者填補為其他適當的值

    # 確保數據是數字格式
    heatmap_data = heatmap_data.apply(pd.to_numeric, errors='coerce')

    # 確保填充 NaN 為數字值
    heatmap_data = heatmap_data.fillna(0)

    # 繪製熱圖
    plt.figure(figsize=(10, 8))
    sns.heatmap(heatmap_data.astype(float), annot=True, cmap='coolwarm', fmt=".3f", cbar_kws={'label': 'Average Angular Velocity (°/s)'},annot_kws={"size": 8})
    
    # 設置 x 軸在圖表上方
    plt.xticks(ticks=np.arange(len(x_labels)), labels=x_labels, rotation=0, ha='left')
    plt.yticks(rotation=0)
    plt.xlabel("Tasks")
    plt.ylabel("neurons")
    plt.title("Neuron Lesion")

    # 顯示圖表
    plt.tight_layout()
    plt.savefig("heatmap.png")

# 假設你有 4 個 CSV 檔案
file_list = ["PG.csv", "RS.csv", "AG.csv", "FS.csv"]

x_labels = ["Pro-goal","Rarestalemate","Anti-goal","Frontstalemate",]

# 使用你提供的 y 軸順序
y_order = [
    'xLAL010', 'xLAL014', 'xLAL018', 'xLAL040', 'xLAL046', 
    'xLAL121', 'xLAL073', 'xLAL122', 'xLAL126', 'xLAL017', 
    'xLAL153', 'Fullmodel'
]

# 讀取資料並創建熱圖
data_dict = load_csv_data(file_list)
create_heatmap(data_dict)
