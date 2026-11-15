import numpy as np


def create_terrain_grid(obstacle_mask, rough_mask=None, cell_size=10):
    """
    
    """


    if obstacle_mask is None:
        raise ValueError("Obstacle mask cannot be None.")
    
    height, width = obstacle_mask.shape  # Get image dimensions .shape

    num_rows = height // cell_size
    num_cols = width // cell_size

    grid = [ ]
    for _ in range(num_rows):
        grid.append([1] * num_cols)  # Initialize each cell as safe terrain (1)

    for row in range(num_rows):
        for col in range(num_cols):

            # Calculate the pixel boundaries for the current cell
            y_start = row * cell_size
            y_end = y_start + cell_size
            x_start = col * cell_size 
            x_end = x_start + cell_size

            # Extract the corresponding image section
            cell_mask = obstacle_mask[y_start:y_end, x_start:x_end]

            obstacle_count = np.count_nonzero(cell_mask)  # Count non-white pixels
            total_pixels = cell_mask.size   # Total number of pixels in the cell
            obstacle_percentage = (obstacle_count / total_pixels) * 100   # Calculate the percentage of obstacle pixels

            # Classify the cell based on obstacle percentage and rough terrain
            if obstacle_percentage > 20: 
                grid[row][col] = 0  # Impassable terrain
            elif rough_mask is not None and rough_mask[y_start:y_end, x_start:x_end].any():  # Check if rough terrain is present in the cell
                grid[row][col] = 2  # Rough terrain
            else:
                grid[row][col] = 1  # Safe terrain
            

    return grid  
