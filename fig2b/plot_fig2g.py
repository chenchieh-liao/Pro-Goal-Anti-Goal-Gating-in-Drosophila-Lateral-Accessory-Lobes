import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu

# 初始化資料列表
arr10 = []
arr30 = []
arr90 = []

ctr10 = []
ctr30 = []
ctr90 = []

noExc10 = []
noExc30 = []
noExc90 = []

# 讀取資料並計算平均值
for data in range(1, 51):
    file10 = pd.read_csv(f'/home/chieh1102/FPLmodel/open-loop_v5/fig2b/data_no101418/dna02_10_0.01_{data}.txt', header=None, delimiter=' ')
    file30 = pd.read_csv(f'/home/chieh1102/FPLmodel/open-loop_v5/fig2b/data_no101418/dna02_30_0.01_{data}.txt', header=None, delimiter=' ')
    file90 = pd.read_csv(f'/home/chieh1102/FPLmodel/open-loop_v5/fig2b/data_no101418/dna02_90_0.01_{data}.txt', header=None, delimiter=' ')
    
    arr10.append(file10[1][5000:8000].mean())
    arr30.append(file30[1][5000:8000].mean())
    arr90.append(file90[1][5000:8000].mean())

    file10ctr = pd.read_csv(f'/home/chieh1102/FPLmodel/open-loop_v5/fig2b/data_ctr/dna02_10_0.01_{data}.txt', header=None, delimiter=' ')
    file30ctr = pd.read_csv(f'/home/chieh1102/FPLmodel/open-loop_v5/fig2b/data_ctr/dna02_30_0.01_{data}.txt', header=None, delimiter=' ')
    file90ctr = pd.read_csv(f'/home/chieh1102/FPLmodel/open-loop_v5/fig2b/data_ctr/dna02_90_0.01_{data}.txt', header=None, delimiter=' ')
    
    ctr10.append(file10ctr[1][5000:8000].mean())
    ctr30.append(file30ctr[1][5000:8000].mean())
    ctr90.append(file90ctr[1][5000:8000].mean())

    file10noExc = pd.read_csv(f'/home/chieh1102/FPLmodel/open-loop_v5/fig2b/data_noExc_connect/dna02_10_0.01_{data}.txt', header=None, delimiter=' ')
    file30noExc = pd.read_csv(f'/home/chieh1102/FPLmodel/open-loop_v5/fig2b/data_noExc_connect/dna02_30_0.01_{data}.txt', header=None, delimiter=' ')
    file90noExc = pd.read_csv(f'/home/chieh1102/FPLmodel/open-loop_v5/fig2b/data_noExc_connect/dna02_90_0.01_{data}.txt', header=None, delimiter=' ')
    
    noExc10.append(file10noExc[1][5000:8000].mean())
    noExc30.append(file30noExc[1][5000:8000].mean())
    noExc90.append(file90noExc[1][5000:8000].mean())

# 準備繪製箱形圖的資料
data = [arr10, noExc10, ctr10, arr30, noExc30, ctr30, arr90, noExc90, ctr90]
labels = ['- Exc.core', '- Exc.core connect', 'Full model', 
          '- Exc.core', '- Exc.core connect', 'Full model', 
          '- Exc.core', '- Exc.core connect', 'Full model']

# 定義修正後的 positions，並使用較小的 widths 值
positions = [0.7, 1, 1.3,  # 10˚
             2.2, 2.5, 2.8,  # 30˚
             3.7, 4, 4.3]  # 90˚

# 新增參數來調整線條粗細
line_width = 4  # 線條粗細
box_line_width = 4  # 箱形圖的線條粗細
axis_line_width = 4  # 軸的線條粗細

# 繪製箱形圖，設定較小的 box 寬度
plt.figure(figsize=(20, 17), dpi=500)
plt.boxplot(
    data,
    positions=positions,
    widths=0.3,
    patch_artist=True,
    boxprops=dict(facecolor='lightblue', linewidth=box_line_width),
    medianprops=dict(color='red', linewidth=box_line_width),
    whiskerprops=dict(linewidth=box_line_width),
    capprops=dict(linewidth=box_line_width),
    flierprops=dict(markerfacecolor='orange', markersize=5, linewidth=box_line_width)
)

# 在 box 下方添加分組標籤
group_labels = ['10˚', '30˚', '90˚']
group_positions = [1, 2.5, 4]  # 每組的中央位置

# 計算所有資料的最大值和最小值，供標籤定位使用
all_data = arr10 + arr30 + arr90 + ctr10 + ctr30 + ctr90 + noExc10 + noExc30 + noExc90
max_y = max(all_data)
min_y = min(all_data)

for i, label in enumerate(group_labels):
    plt.text(group_positions[i], 0.8,  # 根據資料調整高度
             label, ha='center', fontsize=45, fontweight='bold')

# 自訂 x 軸刻度和標籤
plt.xticks(positions, labels, rotation=60, ha='right', fontsize=45)
plt.yticks(fontsize=45)
plt.ylim(0,1.1)

# 添加軸標籤和標題
plt.ylabel('Mean Firing Rate Difference of DNa02', fontsize=40)
# plt.title('Boxplot of Mean Firing Rates by Angle and Condition', fontsize=40)

# 調整軸的線條粗細
plt.gca().spines['top'].set_linewidth(axis_line_width)
plt.gca().spines['right'].set_linewidth(axis_line_width)
plt.gca().spines['left'].set_linewidth(axis_line_width)
plt.gca().spines['bottom'].set_linewidth(axis_line_width)

# 添加網格線和調整布局
plt.tight_layout(rect=[0.01, 0.01, 0.99, 0.99])  # 增加邊界空間
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# 儲存並顯示圖形
plt.savefig('fig2G.png')
