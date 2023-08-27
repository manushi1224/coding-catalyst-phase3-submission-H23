import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Load data from CSV file
yard_df = pd.read_csv('yard_final.csv') 

# Define the dimensions of a single compartment 
compartment_rows = 1
compartment_bays = 6  # Change the number of bays per compartment
compartment_tiers = yard_df['Level'].max()

# Define the data to be plotted
data_to_plot = yard_df[(yard_df['Area'] == 'A') & (yard_df['Level'] >= 3) & (yard_df['Level'] <= 4)]  

# Create a dictionary to map areas to unique colors or patterns
area_colors = {
    'A': 'r',  
    'B': 'g',  
    'C': 'b',  
    'D': 'c',  
    'E': 'r', 
    'F': 'g',  
    'G': 'c',
    'H': 'orange',
    'I': 'purple',
    'J': 'lime',
    'K': 'pink',
    'L': 'brown'
}

# Create a new figure
fig = plt.figure(figsize=(10, 8))  # Adjust the figsize as needed
ax = fig.add_subplot(111, projection='3d')

# Plot all possible points in the yard (up to tier 4)
for x in range(data_to_plot['Row'].max() + 1):
    for y in range(ord('A'), ord('L') + 1):
        for z in range(4):  # Limit tiers up to 4
            color = (0.8, 0.8, 0.8, 0.5)  # Semi-transparent light grey color
            ax.bar3d(x, y - ord('A'), z, compartment_rows, compartment_bays, compartment_tiers, color=color)

# Plot the selected data
for _, row in data_to_plot.iterrows():
    x = row['Row'] - 1  
    y = ord(row['Bay']) - ord('A')  
    z = row['Level'] - 1

    color = area_colors.get(row['Area'], 'k') 

    ax.bar3d(x, y, z, compartment_rows, compartment_bays, compartment_tiers, shade=True, color=color)

ax.set_xlabel('Rows')
ax.set_ylabel('Bays')
ax.set_zlabel('Tiers')
ax.set_title('Empty spaces in yard')

# Show the plot
plt.show()

