import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Load data from CSV file
yard_df = pd.read_csv('yard_final.csv')  # Make sure the file path is correct

# Get unique areas from the DataFrame
unique_areas = yard_df['Area'].unique()

# Define the dimensions of a single compartment
compartment_rows = 1
compartment_bays = 6  # Change the number of bays per compartment
compartment_tiers = yard_df['Level'].max()

# Define the minimum tier to include objects
min_tier = 3  # Change this value to your desired minimum tier

# Create a dictionary to map areas
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

# Create a new figure for all areas
fig = plt.figure(figsize=(10, 8))  # Adjust the figsize as needed
ax = fig.add_subplot(111, projection='3d')

# Sort the compartments based on their areas and bay ranges
sorted_compartments = sorted(unique_areas, key=lambda x: (x, int(x[1:]) if x[1:].isdigit() else float('inf')))

# Plot all compartments
for idx, area in enumerate(sorted_compartments):
    # Filter the DataFrame
    area_df = yard_df[(yard_df['Area'] == area) & (yard_df['Level'] >= min_tier)]

    # Calculate the bay range 
    start_bay = 1 + idx * compartment_bays
    end_bay = start_bay + compartment_bays - 1

    if not area_df.empty:
        yard_rows = area_df['Row'].max() + 1
        yard_bays = end_bay - start_bay + 1  # Adjusted number of bays
        yard_tiers = area_df['Level'].max()
        
        yard = np.zeros((yard_rows, yard_bays, yard_tiers), dtype=int)

        for _, row in area_df.iterrows():
            x = row['Row'] - 1  
            y = (ord(row['Bay']) - ord('A')) - start_bay  # Adjusted bay index
            z = row['Level'] - 1

            color = area_colors.get(area, 'k')  

            ax.bar3d(x, y, z, compartment_rows, 1, compartment_tiers, shade=True, color=color)

ax.set_xlabel('Rows')
ax.set_ylabel('Bays')
ax.set_zlabel('Tiers')
ax.set_title('Yard')

# Show all compartments on a single page
plt.show()
