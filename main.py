"""
1. Load the terrain image.
2. Process the image to identify obstacles.
3. Convert the obstacle mask into a grid.
4. Define the rover's starting position and destination.
5. Run the A* pathfinder.
6. Display the resulting route.
7. Print whether a valid path was found.
"""

# main.py

# Import functions from other modules.
from image_processor import process_image
from terrain_mapper import create_terrain_grid
from rover_navigation import find_path
from interface import display_results


# STEP 1: PROCESS IMAGE
folder_path = "images"
image = process_image(folder_path)
print(len(image))
for i in range(len(image)):
    obstacle_mask = image[i]
    # STEP 2: GENERATE TERRAIN GRID
    grid = create_terrain_grid(
        obstacle_mask,
        rough_mask=None,
        cell_size=10)

    # STEP 3: DEFINE START AND DESTINATION
    start = (0, 0)
    goal = (len(grid[0]) - 1, len(grid) - 1)

    # STEP 4: FIND INITIAL ROUTE
    path = find_path(grid, start, goal)
    if path is None:
        print("No valid route found!")

    else:
        print("Initial route:", path)

    display_results(image[i], grid, path, start, goal)
