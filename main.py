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
image = process_image()
for i in image:
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

    # ========================================================
    # STEP 6: DISPLAY RESULTS
    # ========================================================

    print("\n--- MISSION REPORT ---")

    print("Mission completed:", results["completed"])

    print(
        "Final position:",
        results["final_position"]
    )

    print(
        "Battery remaining:",
        results["battery_remaining"]
    )

    print(
        "Distance travelled:",
        results["distance_travelled"]
    )

    print("Events:")

    for event in results["events"]:
        print("-", event)

    # Display the final terrain and travelled route.
    display_results(
        results["final_grid"],
        results["route_taken"],
        start,
        goal,
        results["final_position"]
    )
