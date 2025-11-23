import pandas as pd
import matplotlib.pyplot as plt

# 讀取 CSV
df = pd.read_csv('diff&sum.csv')
print(df.columns.tolist())
# 建立圖表
fig, ax1 = plt.subplots(figsize=(12, 6))

labels = df['Label']
x = range(len(labels))

# 畫差異的柱狀圖（左軸）
color1 = 'tab:red'
ax1.set_xlabel('Model')
ax1.set_ylabel('R&L firing rate difference', color=color1)
bars1 = ax1.bar(x, df['R&L firing rate difference'], width=0.4, color=color1, align='center', label='Difference')
ax1.tick_params(axis='y', labelcolor=color1)

# 建立右邊的 y 軸
ax2 = ax1.twinx()
color2 = 'tab:blue'
ax2.set_ylabel('R&L firing rate sum', color=color2)
bars2 = ax2.bar([i + 0.4 for i in x], df['R&L firing rate sum'], width=0.4, color=color2, align='center', label='Sum')
ax2.tick_params(axis='y', labelcolor=color2)

# x 軸標籤
plt.xticks([i + 0.2 for i in x], labels, rotation=30, ha='right')

# 加上圖例
fig.legend(loc='upper right', bbox_to_anchor=(1, 1), bbox_transform=ax1.transAxes)

# 加上標題
plt.title('R&L Firing Rate: Difference vs. Sum')

# 儲存圖片
plt.tight_layout()
plt.savefig('firing_rate_comparison.png')
plt.show()
