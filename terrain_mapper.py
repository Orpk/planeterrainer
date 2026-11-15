import numpy as np


def create_terrain_grid(obstacle_mask, rough_mask=None, cell_size=10):
    """
    STEP 1: Get the image dimensions.
        - Use obstacle_mask.shape.
        - Remember that image dimensions are (height, width).

    STEP 2: Calculate the number of grid rows and columns.
        - Divide image height and width by cell_size.
        - Use integer division (//).

    STEP 3: Create an empty 2D Python list.
        - Each row represents a row of terrain cells.
        - Each column represents a terrain cell.
        - Initially, assign every cell a value of 1 (safe).

    STEP 4: Examine each grid cell.
        - Use nested for loops.
        - Extract the corresponding image section.
        - Use NumPy slicing:
          mask[y_start:y_end, x_start:x_end]

    STEP 5: Calculate the percentage of obstacle pixels.
        - Count white pixels using np.count_nonzero().
        - Divide by the total number of pixels in the cell.

    STEP 6: Classify the cell.
        - If obstacle percentage exceeds 20%, assign 0.
        - Otherwise, if rough_mask indicates rough terrain, assign 2.
        - Otherwise, assign 1.

    STEP 7: Return the completed terrain grid.

    GUIDE:
    https://numpy.org/doc/stable/user/quickstart.html
    """


    # TODO 1: Get image height and width.

    # TODO 2: Calculate grid dimensions.

    # TODO 3: Initialize a 2D list filled with safe terrain (1).

    # TODO 4: Loop through every grid cell.

    # TODO 5: Extract the corresponding image section.

    # TODO 6: Calculate the obstacle percentage.

    # TODO 7: Assign terrain costs based on classification.

    # TODO 8: Return the grid.

    pass