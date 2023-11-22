import geopandas as gpd
import matplotlib.pyplot as plt
import os

file = r"D:\shapefiles\Dataset\Islamabad"

y = [d for d in os.listdir(file) if d.endswith(".shp")]

fig, axs = plt.subplots(4, 2, figsize=(12, 12))  # Create a 4x2 subplot grid
fig.patch.set_facecolor('black')
plt.suptitle("Plotting and Analyzing Shapefiles: Islamabad Dataset Visualization", fontsize = 16, fontweight= "bold", color= "grey", y = 1)

for index, d in enumerate(y[:8]):  # Limit to the first 8 shapefiles
    shp = os.path.join(file, d)
    gdf = gpd.read_file(shp)

    ax = axs[index // 2, index % 2]  # Get the current subplot

    ax.set_facecolor('white')
    gdf.plot(ax=ax, color='white', edgecolor='black')  # Plot with appropriate colors

    ax.set_title(os.path.basename(shp).replace("_", " ").replace(".shp", ""), color='white', fontsize=12)
    ax.axis('off')

    # Adding border
    border_color = 'white'
    border_width = 2
    
    # Add border as a Rectangle patch
    rect = plt.Rectangle((0, 0), 1, 1, transform=ax.transAxes, linewidth=border_width,
                         edgecolor=border_color, facecolor='none')
    ax.add_patch(rect)

    # Set aspect ratio to make each subplot square
    x0, x1 = ax.get_xlim()
    y0, y1 = ax.get_ylim()
    new_height = abs(x1 - x0) * 0.1
    new_width = abs(y1 - y0) * 0.1
    ax.set_aspect((new_height / new_width) * 0.5)

plt.tight_layout()  # Adjust subplot layout
# plt.show()  # Show the combined plot with subplots

# save map
plt.savefig("shp_reading 1" + ".png")

