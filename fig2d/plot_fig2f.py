import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

LEN = 8000

arr10 = []
arr30 = []
arr90 = []
arr120 = []

ctr10 = []
ctr30 = []
ctr90 = []
ctr120 = []

arr210 = []
arr230 = []
arr290 = []
arr2120 = []

for data in range(1, 51):
    file10 = pd.read_csv(f'/home/chieh1102/FPLmodel/open-loop_v5/fig2d/data_no040/dna02_10_0.01_{data}.txt', header=None, delimiter=' ')
    file30 = pd.read_csv(f'/home/chieh1102/FPLmodel/open-loop_v5/fig2d/data_no040/dna02_30_0.01_{data}.txt', header=None, delimiter=' ')
    file90 = pd.read_csv(f'/home/chieh1102/FPLmodel/open-loop_v5/fig2d/data_no040/dna02_90_0.01_{data}.txt', header=None, delimiter=' ')
    #file120 = pd.read_csv(f'/home/chieh1102/FPLmodel/open-loop_v5/fig2b/data_no1014/dna02_120_0.01_{data}.txt', header=None, delimiter=' ')
    arr10.append(file10[1][0:8000])
    arr30.append(file30[1][0:8000])
    arr90.append(file90[1][0:8000])
    #arr120.append(file120[1][0:8000])
    file10ctr = pd.read_csv(f'/home/chieh1102/FPLmodel/open-loop_v5/fig2b/data_ctr/dna02_10_0.01_{data}.txt', header=None, delimiter=' ')
    file30ctr = pd.read_csv(f'/home/chieh1102/FPLmodel/open-loop_v5/fig2b/data_ctr/dna02_30_0.01_{data}.txt', header=None, delimiter=' ')
    file90ctr = pd.read_csv(f'/home/chieh1102/FPLmodel/open-loop_v5/fig2b/data_ctr/dna02_90_0.01_{data}.txt', header=None, delimiter=' ')
    #file120ctr = pd.read_csv(f'/home/chieh1102/FPLmodel/open-loop_v5/fig2d/data_no040/dna02_120_0.01_{data}.txt', header=None, delimiter=' ')
    ctr10.append(file10ctr[1][0:8000])
    ctr30.append(file30ctr[1][0:8000])
    ctr90.append(file90ctr[1][0:8000])
    #ctr120.append(file120ctr[1][0:8000])
    file10arr = pd.read_csv(f'/home/chieh1102/FPLmodel/open-loop_v5/fig2d/data_no121/dna02_10_0.01_{data}.txt', header=None, delimiter=' ')
    file30arr = pd.read_csv(f'/home/chieh1102/FPLmodel/open-loop_v5/fig2d/data_no121/dna02_30_0.01_{data}.txt', header=None, delimiter=' ')
    file90arr = pd.read_csv(f'/home/chieh1102/FPLmodel/open-loop_v5/fig2d/data_no121/dna02_90_0.01_{data}.txt', header=None, delimiter=' ')
    #file120ctr = pd.read_csv(f'/home/chieh1102/FPLmodel/open-loop_v5/fig2d/data_no121/dna02_120_0.01_{data}.txt', header=None, delimiter=' ')
    arr210.append(file10arr[1][0:8000])
    arr230.append(file30arr[1][0:8000])
    arr290.append(file90arr[1][0:8000])
    #ctr120.append(file120ctr[1][0:8000])

#print(arr10)

df_10 = pd.DataFrame(arr10)
mean10 = df_10.mean(axis=0)
std10 = df_10.std(axis=0)

df2_10 = pd.DataFrame(arr210)
mean210 = df2_10.mean(axis=0)
std210 = df2_10.std(axis=0)

df_10ctr = pd.DataFrame(ctr10)
mean10ctr = df_10ctr.mean(axis=0)
std10ctr = df_10ctr.std(axis=0)

df_30 = pd.DataFrame(arr30)
mean30 = df_30.mean(axis=0)
std30 = df_30.std(axis=0)

df2_30 = pd.DataFrame(arr230)
mean230 = df2_30.mean(axis=0)
std230 = df2_30.std(axis=0)

df_30ctr = pd.DataFrame(ctr30)
mean30ctr = df_30ctr.mean(axis=0)
std30ctr = df_30ctr.std(axis=0)

df_90 = pd.DataFrame(arr90)
mean90 = df_90.mean(axis=0)
std90 = df_90.std(axis=0)

df2_90 = pd.DataFrame(arr290)
mean290 = df2_90.mean(axis=0)
std290 = df2_90.std(axis=0)

df_90ctr = pd.DataFrame(ctr90)
mean90ctr = df_90ctr.mean(axis=0)
std90ctr = df_90ctr.std(axis=0)

# df_120 = pd.DataFrame(arr120)
# mean120 = df_120.mean(axis=0)
# std120 = df_120.std(axis=0)

# df_120ctr = pd.DataFrame(ctr120)
# mean120ctr = df_120ctr.mean(axis=0)
# std120ctr = df_120ctr.std(axis=0)

x = []

for k in range(8000):
    x.append(k/10)

plt.figure(dpi=300, figsize=[13, 10])
# plt.plot(x, mean10, label='10˚, no Exc. core output', color='blue',linewidth=8)
plt.plot(x, mean30, label='30˚, - LAL040 output', linestyle='--', color='orange',linewidth=8)
plt.plot(x, mean90, label='90˚, - LAL040 output',  linestyle='--', color='green',linewidth=8)
# plt.plot(x, mean120, label='120˚, no 010&014', color='red')
# plt.plot(x, mean10ctr, label='10˚, full model', linestyle='--', color='blue',linewidth=8)
plt.plot(x, mean30ctr, label='30˚, full model',  color='orange',linewidth=8)
plt.plot(x, mean90ctr, label='90˚, full model', color='green',linewidth=8)
# plt.plot(x, mean120ctr, label='120˚, full model', linestyle='--', color='red')
#plt.legend(fontsize = 18)
plt.plot(x, mean230, label='30˚, - LAL121 output',linestyle=':', color='orange',linewidth=8)
plt.plot(x, mean290, label='90˚, - LAL121 output',linestyle=':', color='green',linewidth=8)

plt.xlabel('Time (ms)', fontsize=45)
plt.ylabel('DNa02 firing rate difference', fontsize=45)
xticks = np.arange(0, 820, 200)
plt.yticks(fontsize=40)
plt.xticks(xticks,fontsize=40)
plt.ylim(0,1.0)
plt.tick_params(axis='both', which='both', width=4, length=10)  # 設定刻度線的粗細和長度

# 去掉圖表邊框，只保留 X 和 Y 軸
ax = plt.gca()
ax.spines['top'].set_visible(False)  # 隱藏上邊框
ax.spines['right'].set_visible(False)  # 隱藏右邊框
ax.spines['left'].set_linewidth(4)  # 加粗 Y 軸線條
ax.spines['bottom'].set_linewidth(4.0)  # 加粗 X 軸線條

plt.tight_layout(rect=[0.03, 0.03, 0.97, 0.97])  # 增加邊界空間
plt.savefig('fig2G_v3.svg')

# import matplotlib.pyplot as plt

# # Plot boxplot for all conditions (arr and ctr data)
# data = [df_10.values.flatten(), df_10ctr.values.flatten(),
#         df_30.values.flatten(), df_30ctr.values.flatten(),
#         df_90.values.flatten(), df_90ctr.values.flatten(),
#         ]



# # Define labels for the conditions
# labels = ['10˚ \n No Exc. core', '10˚ \n Full model', '30˚ \n No Exc. core', '30˚ \n Full model', '90˚ \n No Exc. core', '90˚ \n Full model']

# # Create a boxplot
# plt.figure(figsize=(10, 6), dpi=100)
# plt.boxplot(data, labels=labels, patch_artist=True, 
#             boxprops=dict(facecolor='lightblue', color='black'),
#             whiskerprops=dict(color='black'), capprops=dict(color='black'),
#             medianprops=dict(color='red'))

# # Add title and labels
# #plt.title('Boxplot of Firing Rates across Conditions', fontsize=18)
# plt.xlabel('Conditions', fontsize=16)
# plt.ylabel('Firing Rate Difference of DNa02', fontsize=16)

# # Customize x-ticks and y-ticks
# plt.xticks(fontsize=14)
# plt.yticks(fontsize=14)

# # Display the boxplot
# plt.tight_layout()
# plt.savefig('boxplot.png')


# import numpy as np
# import matplotlib.pyplot as plt

# # Create labels for x-axis
# labels = ['10˚', '30˚', '90˚', '120˚']

# # Means for the experimental data
# means = [mean10.mean(), mean30.mean(), mean90.mean()]
# # Standard deviations for the experimental data
# stds = [std10.mean(), std30.mean(), std90.mean()]

# # Means for the control data
# means_ctr = [mean10ctr.mean(), mean30ctr.mean(), mean90ctr.mean()]
# # Standard deviations for the control data
# stds_ctr = [std10ctr.mean(), std30ctr.mean(), std90ctr.mean()]

# # X positions for the bars
# x = np.arange(len(labels))  # the label locations
# width = 0.35  # width of the bars

# # Create the figure and axes
# fig, ax = plt.subplots(figsize=(10, 6))

# # Plot bars for the experimental data
# bar1 = ax.bar(x - width/2, means, width, yerr=stds, label='remove 010&014', capsize=5, color='lightblue')

# # Plot bars for the control data
# bar2 = ax.bar(x + width/2, means_ctr, width, yerr=stds_ctr, label='Full model', capsize=5, color='orange')

# # Add labels, title, and custom x-axis tick labels
# ax.set_xlabel('Condition', fontsize=16)
# ax.set_ylabel('Mean Firing Rate Difference of DNa02', fontsize=16)
# ax.set_title('Comparison of Firing Rates ', fontsize=18)
# ax.set_xticks(x)
# ax.set_xticklabels(labels, fontsize=14)
# ax.legend(fontsize=14)

# # Show plot
# plt.tight_layout()
# plt.savefig('t.png')

# import numpy as np
# import matplotlib.pyplot as plt

# # Number of samples (N)
# N = 400

# # Means for the experimental data
# means = [mean10.mean(), mean30.mean(), mean90.mean(), mean120.mean()]
# # Standard errors for the experimental data
# sem_exp = [std10.mean()/np.sqrt(N), std30.mean()/np.sqrt(N), std90.mean()/np.sqrt(N), ]

# # Means for the control data
# means_ctr = [mean10ctr.mean(), mean30ctr.mean(), mean90ctr.mean(), mean120ctr.mean()]
# # Standard errors for the control data
# sem_ctr = [std10ctr.mean()/np.sqrt(N), std30ctr.mean()/np.sqrt(N), std90ctr.mean()/np.sqrt(N)]

# # X positions for the bars
# x = np.arange(4)  # 4 conditions
# width = 0.35  # width of the bars

# # Create the figure and axes
# fig, ax = plt.subplots(figsize=(10, 6))

# # Plot bars for the experimental data
# bar1 = ax.bar(x - width/2, means, width, yerr=sem_exp, label='remove 010&014', capsize=5, color='lightblue')

# # Plot bars for the control data
# bar2 = ax.bar(x + width/2, means_ctr, width, yerr=sem_ctr, label='Full model', capsize=5, color='orange')

# # Add labels, title, and custom x-axis tick labels
# ax.set_xlabel('Condition', fontsize=16)
# ax.set_ylabel('Mean Firing Rate Difference of DNa02', fontsize=16)
# ax.set_title('Comparison of Firing Rates', fontsize=18)
# ax.set_xticks(x)
# ax.set_xticklabels(['10˚', '30˚', '90˚', '120˚'], fontsize=14)
# ax.legend(fontsize=14)

# # Show plot
# plt.tight_layout()
# plt.savefig('a.png')

