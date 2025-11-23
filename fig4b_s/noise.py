import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, ks_2samp

# 讀取數據
file_LAL010 = '/home/chieh1102/FPLmodel/open-loop_v5/fig4b_s/noise/dna02_0_0.07_LAL010_8.txt'
file_LAL153 = '/home/chieh1102/FPLmodel/open-loop_v5/fig4b_s/noise/dna02_0_0.07_LAL153_8.txt'

# 每行格式: index value
data_LAL010 = np.loadtxt(file_LAL010, usecols=1)
data_LAL153 = np.loadtxt(file_LAL153, usecols=1)

# 只取 6500–8000 筆資料
data_LAL010 = data_LAL010[6500:8001]  # slice 是 [start:end)，所以要 +1
data_LAL153 = data_LAL153[6500:8001]

# 標準化
data_LAL010_z = (data_LAL010 - np.mean(data_LAL010)) / np.std(data_LAL010)
data_LAL153_z = (data_LAL153 - np.mean(data_LAL153)) / np.std(data_LAL153)

# 畫分布 + Gaussian fit
for data, label, color in zip([data_LAL010, data_LAL153],
                              ['LAL010 (I_pfl3)', 'LAL153 (I)'],
                              ['blue', 'red']):
    # fit Gaussian
    mu, std = norm.fit(data)

    # 畫直方圖
    plt.hist(data, bins=50, density=True, alpha=0.6, color=color, label=f"{label} data")

    # 畫 Gaussian 曲線
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, color=color, linewidth=2, linestyle='--',
             label=f"{label} fit: μ={mu:.2f}, σ={std:.2f}")

plt.xlabel("I value")
plt.ylabel("Probability Density")
plt.title("Distribution (samples 6500–8000)")
plt.legend()
plt.savefig('distribution_6500-8000.png')

# Gaussian fit
mu1, std1 = norm.fit(data_LAL010)
mu2, std2 = norm.fit(data_LAL153)

print(f"LAL010: μ={mu1:.3f}, σ={std1:.3f}")
print(f"LAL153: μ={mu2:.3f}, σ={std2:.3f}")

# KS 檢定
stat, p_value = ks_2samp(data_LAL010, data_LAL153)
print(f"KS test: stat={stat:.3f}, p={p_value:.3g}")

# 畫圖
plt.figure(figsize=(8,6))

# 重疊直方圖
bins = 30
plt.hist(data_LAL010, bins=bins, density=True, alpha=0.5, label="LAL010 (I_pfl3)")
plt.hist(data_LAL153, bins=bins, density=True, alpha=0.5, label="LAL153 (I)")

# 畫 Gaussian 曲線
xmin = min(data_LAL010.min(), data_LAL153.min())
xmax = max(data_LAL010.max(), data_LAL153.max())
x = np.linspace(xmin, xmax, 200)

p1 = norm.pdf(x, mu1, std1)
p2 = norm.pdf(x, mu2, std2)

plt.plot(x, p1, 'b-', linewidth=2, label=f"LAL010 fit μ={mu1:.2f}, σ={std1:.2f}")
plt.plot(x, p2, 'r-', linewidth=2, label=f"LAL153 fit μ={mu2:.2f}, σ={std2:.2f}")

plt.xlabel("Value")
plt.ylabel("Density")
plt.title("Distribution Comparison: LAL010 vs LAL153")
plt.legend()
plt.grid(True)
plt.savefig('distribution_comparison.png')

# Gaussian fit
mu1, std1 = norm.fit(data_LAL010_z)
mu2, std2 = norm.fit(data_LAL153_z)

print(f"Standardized LAL010: μ={mu1:.3f}, σ={std1:.3f}")
print(f"Standardized LAL153: μ={mu2:.3f}, σ={std2:.3f}")

# KS 檢定
stat, p_value = ks_2samp(data_LAL010_z, data_LAL153_z)
print(f"KS test (standardized): stat={stat:.3f}, p={p_value:.3g}")

# 畫重疊直方圖 + Gaussian 曲線
plt.figure(figsize=(8,6))

bins = 30
plt.hist(data_LAL010_z, bins=bins, density=True, alpha=0.5, label="LAL010 (I_pfl3)")
plt.hist(data_LAL153_z, bins=bins, density=True, alpha=0.5, label="LAL153 (I)")

xmin = min(data_LAL010_z.min(), data_LAL153_z.min())
xmax = max(data_LAL010_z.max(), data_LAL153_z.max())
x = np.linspace(xmin, xmax, 200)

p1 = norm.pdf(x, mu1, std1)
p2 = norm.pdf(x, mu2, std2)

plt.plot(x, p1, 'b-', linewidth=2, label=f"LAL010 fit μ={mu1:.2f}, σ={std1:.2f}")
plt.plot(x, p2, 'r-', linewidth=2, label=f"LAL153 fit μ={mu2:.2f}, σ={std2:.2f}")

plt.xlabel("Standardized Value (z-score)")
plt.ylabel("Density")
plt.title("Standardized Distribution Comparison: LAL010 vs LAL153")
plt.legend()
plt.grid(True)
plt.savefig('distribution_standardized_comparison.png')