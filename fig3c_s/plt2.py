import matplotlib.pyplot as plt
import os

# Settings for uniform line and axis thickness
line_width = 4  # Line thickness
axis_width = 3  # Axis thickness

# Define folder
folder = '/home/chieh1102/FPLmodel/open-loop_v5/fig3c/data_ctr'

# Define files for both 0.01 and 0.07 conditions
file_template = 'dna02_180_{:.2f}_{}.txt'
labels = ['DNa02', 'LAL018', 'LAL040', 'LAL121']
conditions = [0.01, 0.07]

# Define base colors
base_colors = {
    'Left side': 'blue',
    'Right side': 'red'
}

# Define line styles
linestyles = {
    0.01: '-',  # solid
    0.07: '--'  # dashed
}

# Define alpha for faded color
alphas = {
    0.01: 1.0,   # strong color
    0.07: 0.5    # faded color
}

# Create subplots
fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(18, 5), sharey=False)
axes = axes.flatten()

for i, (ax, label) in enumerate(zip(axes, labels)):
    for cond in conditions:
        file = os.path.join(folder, file_template.format(cond, label))
        x, y1, y2 = [], [], []
        with open(file, 'r') as f:
            for line in f:
                data = line.strip().split()
                x.append(int(data[0]) / 10)
                y1.append(float(data[1]))
                y2.append(float(data[2]))

        # Plot left and right side with alpha-adjusted colors
        ax.plot(
            x, y1,
            label=f'Left {cond}',
            color=base_colors['Left side'],
            linestyle=linestyles[cond],
            linewidth=line_width,
            alpha=alphas[cond]
        )
        ax.plot(
            x, y2,
            label=f'Right {cond}',
            color=base_colors['Right side'],
            linestyle=linestyles[cond],
            linewidth=line_width,
            alpha=alphas[cond]
        )

    ax.set_title(label, fontsize=24)
    ax.set_ylim(0, 1.0)

    if i == 0:
        ax.set_ylabel('Firing rate', fontsize=22)
        ax.set_xlabel('Time (ms)', fontsize=22)
        ax.tick_params(axis='both', labelsize=16, width=3, length=7)
    else:
        ax.tick_params(labelleft=False, labelbottom=False, width=3, length=7)
        ax.set_yticks([])

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    if i != 0:
        ax.spines['left'].set_visible(False)

    for spine in ax.spines.values():
        spine.set_linewidth(axis_width)

# Add legend
handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, loc='center right', fontsize=16, frameon=False, bbox_to_anchor=(0.99, 0.5))

# Global title and layout
fig.suptitle('Full model Δθ = 180°', fontsize=28)
plt.tight_layout(rect=[0, 0.1, 0.85, 0.99])

# Save and show
plt.savefig('fig3c_full_180_combined.svg')
plt.show()
