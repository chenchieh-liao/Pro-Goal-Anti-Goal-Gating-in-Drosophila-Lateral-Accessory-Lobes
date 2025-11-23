import matplotlib.pyplot as plt
import numpy as np

# Updated labels
pfl_labels_expanded = ["PFL3_L", "PFL3_R", "PFL2_L", "PFL2_R"]

# Data for firing rates at 175° and 180°
angles = [175, 180]

# Firing rate data (PFL and DNa)
pfl_data_corrected = {
    175: [0.25, 0.35, 0.65, 0.65],  # PFL firing rates at 175°
    180: [0.25, 0.25, 0.8, 0.8],  # PFL firing rates at 180°
}
dna_diff_data = {
    175: 0.28599673775335915,  # Difference for DNa02 at 175°
    180: 3.3306690738754696e-16,  # Difference for DNa02 at 180°
}

dna_noPFL2_diff_data = {
    175: 0.027698892018350782,  # Difference for DNa02 at 175°
    180: 1.3877787807814457e-17,  # Difference for DNa02 at 180°
}

# Indices for PFL labels
pfl_indices = np.arange(len(pfl_labels_expanded))

# Bar width for grouped bars
bar_width = 0.35

# Create subplots
fig, axs = plt.subplots(2, 1, figsize=(8, 10))

for i, angle in enumerate(angles):
    ax = axs[i]
    
    # Plot PFL firing rates
    ax.bar(pfl_indices, pfl_data_corrected[angle], bar_width )
    
    # Plot DNa02 firing rate difference
    ax.bar(len(pfl_labels_expanded), dna_diff_data[angle], bar_width, color='orange')
    
    # Plot DNa02 firing rate difference
    ax.bar(len(pfl_labels_expanded)+1, dna_noPFL2_diff_data[angle], bar_width, color='orange')
    
    # Chart configurations
    ax.set_title(f"Δθ = {angle}°",fontsize = 30)
    # 設定 x 軸刻度位置（含 PFL 的 index 與額外的兩個標籤位置）
    ax.set_xticks(np.concatenate([pfl_indices, [len(pfl_labels_expanded), len(pfl_labels_expanded)+1]]))

    # 設定 x 軸標籤文字（包含擴充後的 PFL 標籤 + 兩個附加的標籤）
    ax.set_xticklabels(
        pfl_labels_expanded + ["DNa02 L-R"] + ["DNa02 L-R\nwithout PFL2"], 
        rotation=45, 
        fontsize=25
    )
    # ax.set_xlabel("Neuron Groups")
    
    # Remove y-axis ticks and labels but keep the axis line
    ax.yaxis.set_ticks([])  # Remove ticks
    ax.yaxis.label.set_visible(False)  # Remove label

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    # Make bottom and left spines thicker
    ax.spines['bottom'].set_linewidth(3)
    ax.spines['left'].set_linewidth(3)


    ax.grid(False)
    # ax.legend()

# Adjust layout and display the plot
plt.tight_layout()
plt.savefig('fig3B_v3.png')
