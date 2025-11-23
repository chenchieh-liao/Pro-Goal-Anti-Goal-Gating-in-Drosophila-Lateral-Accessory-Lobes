import matplotlib.pyplot as plt
import os

# Settings for uniform line and axis thickness
line_width = 4  # Line thickness
axis_width = 3  # Axis thickness

# Define file paths
group1_folders = [
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig3c/data_ctr',
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig3c/data_no121',
    f'/home/chieh1102/FPLmodel/open-loop_v5/fig3c/data_noEC'
]

# Function to generate plots for a given folder
def plot_for_group(folder, output_filename, title):
    output_files = [
        os.path.join(folder, f'dna02_180_0.01_DNa02.txt'),
        os.path.join(folder, f'dna02_180_0.01_LAL018.txt'),
        os.path.join(folder, f'dna02_180_0.01_LAL040.txt'),
        os.path.join(folder, f'dna02_180_0.01_LAL121.txt'),
    ]

    # Create subplots
    fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(18, 5), sharey=False)
    axes = axes.flatten()

    for i, (ax, file) in enumerate(zip(axes, output_files)):
        # Read data from file
        x, y1, y2 = [], [], []
        with open(file, 'r') as f:
            for line in f:
                data = line.strip().split()
                x.append(int(data[0]) / 10)
                y1.append(float(data[1]))
                y2.append(float(data[2]))

        # Plot data
        ax.plot(x, y1, label='Left side', color='blue', linewidth=line_width)
        ax.plot(x, y2, label='Right side', color='red', linewidth=line_width)
        ax.set_title(os.path.basename(file).replace('.txt', '').split('_', 3)[-1], fontsize=24)
        ax.set_ylim(0, 1.0)

        # Set axis ticks and labels
        if i == 0:  # Leftmost subplot
            ax.set_ylabel('Firing rate', fontsize=22)
            ax.set_xlabel('Time (ms)', fontsize=22)
            ax.spines['left'].set_visible(True)
            ax.tick_params(axis='both', labelsize=16, width=3, length=7)
        else:  # Other subplots
            ax.tick_params(labelleft=False, labelbottom=False, width=3, length=7)
            ax.set_yticks([])
            ax.spines['left'].set_visible(False)

        # Remove top and right spines
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        # Adjust axis thickness
        for spine in ax.spines.values():
            spine.set_linewidth(axis_width)

    # Add legend on the right
    handles, labels = ax.get_legend_handles_labels()
    fig.legend(
        handles, 
        labels, 
        loc='center right', 
        fontsize=16, 
        frameon=False, 
        bbox_to_anchor=(0.99, 0.5)  # Adjust legend position
    )

    # Global settings
    fig.suptitle(f'{title} Δθ = 180°', fontsize=28)
    plt.tight_layout(rect=[0, 0.1, 0.85, 0.99])  # Adjust subplot layout

    # Save and show plot
    plt.savefig(output_filename)
    plt.show()

# Generate plots for each group
# plot_for_group(group1_folders[0], 'fig3c_full_180.png', 'Full model')
plot_for_group(group1_folders[1], 'fig3d_no121_180.svg', 'without LAL121 output')
plot_for_group(group1_folders[2], 'fig3d_noEC_180.svg', 'without EC output')
