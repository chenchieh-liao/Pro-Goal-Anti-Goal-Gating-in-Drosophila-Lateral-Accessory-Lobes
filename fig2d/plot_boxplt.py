import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu

# Initialize lists to store data
arr10 = []
arr30 = []
arr90 = []

arr10_121 = []
arr30_121 = []
arr90_121 = []

ctr10 = []
ctr30 = []
ctr90 = []

# Loop through the data files and extract the mean firing rates
for data in range(1, 51):
    file10 = pd.read_csv(f'/home/chieh1102/FPLmodel/open-loop_v5/fig2d/data_no040/dna02_10_0.01_{data}.txt', header=None, delimiter=' ')
    file30 = pd.read_csv(f'/home/chieh1102/FPLmodel/open-loop_v5/fig2d/data_no040/dna02_30_0.01_{data}.txt', header=None, delimiter=' ')
    file90 = pd.read_csv(f'/home/chieh1102/FPLmodel/open-loop_v5/fig2d/data_no040/dna02_90_0.01_{data}.txt', header=None, delimiter=' ')
    
    arr10.append(file10[1][5000:8000].mean())
    arr30.append(file30[1][5000:8000].mean())
    arr90.append(file90[1][5000:8000].mean())

    file10 = pd.read_csv(f'/home/chieh1102/FPLmodel/open-loop_v5/fig2d/data_no121/dna02_10_0.01_{data}.txt', header=None, delimiter=' ')
    file30 = pd.read_csv(f'/home/chieh1102/FPLmodel/open-loop_v5/fig2d/data_no121/dna02_30_0.01_{data}.txt', header=None, delimiter=' ')
    file90 = pd.read_csv(f'/home/chieh1102/FPLmodel/open-loop_v5/fig2d/data_no121/dna02_90_0.01_{data}.txt', header=None, delimiter=' ')
    
    arr10_121.append(file10[1][5000:8000].mean())
    arr30_121.append(file30[1][5000:8000].mean())
    arr90_121.append(file90[1][5000:8000].mean())

    file10ctr = pd.read_csv(f'/home/chieh1102/FPLmodel/open-loop_v5/fig2b/data_ctr/dna02_10_0.01_{data}.txt', header=None, delimiter=' ')
    file30ctr = pd.read_csv(f'/home/chieh1102/FPLmodel/open-loop_v5/fig2b/data_ctr/dna02_30_0.01_{data}.txt', header=None, delimiter=' ')
    file90ctr = pd.read_csv(f'/home/chieh1102/FPLmodel/open-loop_v5/fig2b/data_ctr/dna02_90_0.01_{data}.txt', header=None, delimiter=' ')
    
    ctr10.append(file10ctr[1][5000:8000].mean())
    ctr30.append(file30ctr[1][5000:8000].mean())
    ctr90.append(file90ctr[1][5000:8000].mean())

# Perform the Mann-Whitney U Test for each comparison
u_stat_10, p_value_10 = mannwhitneyu(arr10, ctr10, alternative='two-sided')
u_stat_30, p_value_30 = mannwhitneyu(arr30, ctr30, alternative='two-sided')
u_stat_90, p_value_90 = mannwhitneyu(arr90, ctr90, alternative='two-sided')

# Print out the U statistic and p-value for each comparison
print(f'10˚ comparison - U statistic: {u_stat_10}, p-value: {p_value_10}')
print(f'30˚ comparison - U statistic: {u_stat_30}, p-value: {p_value_30}')
print(f'90˚ comparison - U statistic: {u_stat_90}, p-value: {p_value_90}')

# Prepare data for boxplot, including 121 group
data = [ctr10, arr10, arr10_121, ctr30, arr30, arr30_121, ctr90, arr90, arr90_121]
labels = ['10˚\nFull model', '10˚\nNo 040 output', '10˚\nNo 121 output', 
          '30˚\nFull model', '30˚\nNo 040 output', '30˚\nNo 121 output', 
          '90˚\nFull model', '90˚\nNo 040 output', '90˚\nNo 121 output']

# Create a figure and axis
plt.figure(figsize=(14, 8), dpi=300)

# Create the boxplot with enhanced visualization
box = plt.boxplot(data, patch_artist=True, boxprops=dict(facecolor='lightblue', color='black'), 
                  medianprops=dict(color='darkblue', linewidth=2), whiskerprops=dict(color='black', linewidth=1.5))

# Customize the x-axis with new labels
plt.xticks(range(1, len(labels) + 1), labels, fontsize=12, rotation=45)

# Add axis labels and title
plt.ylabel('Mean Firing Rate Difference of DNa02', fontsize=14)
plt.title('Comparative Analysis of Mean Firing Rates across Conditions', fontsize=16)

# # Highlight p-values on the plot for significant comparisons
# significance_levels = [p_value_10, p_value_30, p_value_90]
# for i, p_val in enumerate(significance_levels, 1):
#     if p_val < 0.05:
#         plt.text(3 * i - 2.5, max(data[3 * i - 3]) + 0.5, f'p = {p_val:.3f}', ha='center', fontsize=10, color='red')

# Adjust layout and save the figure
plt.tight_layout()
plt.savefig('boxplot_means_full_comparison.png')  # Save the plot with enhanced visuals
plt.show()
