# interface.py

def display_results(
    grid,
    route,
    start,
    goal,
    rover_position=None
):
    """
    Display the terrain grid and rover navigation information.

    STEP 1: Import libraries.
        - matplotlib.pyplot for plotting.
        - ListedColormap for custom terrain colours.

    STEP 2: Convert the grid into a NumPy array if necessary.

    STEP 3: Create a colour map.
        - 0 = Black (obstacle)
        - 1 = Green (safe)
        - 2 = Yellow (rocky)
        - 3 = Red (difficult)

    STEP 4: Display the terrain grid.
        - Use ax.imshow().
        - Set vmin=0 and vmax=3.

    STEP 5: Display the route.
        - Extract row and column coordinates from route.
        - Plot columns on the X-axis.
        - Plot rows on the Y-axis.

    STEP 6: Mark important locations.
        - Start: Green marker.
        - Goal: White marker.
        - Rover: Blue marker.

    STEP 7: Add a title, legend, and grid lines.

    STEP 8: Display the completed visualization.

    GUIDE:
    https://matplotlib.org/stable/plot_types/arrays/imshow.html
    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
    """

    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.colors import ListedColormap

    # STEP 1: Convert terrain grid to NumPy array.
    terrain = np.array(grid)

    # STEP 2: Define terrain colours.
    colors = [
        "black",
        "green",
        "yellow",
        "red"
    ]

    terrain_cmap = ListedColormap(colors)

    # STEP 3: Create figure and display terrain.
    fig, ax = plt.subplots(figsize=(9, 7))

    ax.imshow(
        terrain,
        cmap=terrain_cmap,
        vmin=0,
        vmax=3
    )

    # STEP 4: Draw the planned or travelled route.
    if route:

        rows = [position[0] for position in route]
        cols = [position[1] for position in route]

        ax.plot(
            cols,
            rows,
            color="blue",
            linewidth=2,
            label="Rover route"
        )

    # STEP 5: Mark starting point.
    ax.scatter(
        start[1],
        start[0],
        color="lime",
        marker="o",
        s=100,
        label="Start"
    )

    # STEP 6: Mark destination.
    ax.scatter(
        goal[1],
        goal[0],
        color="white",
        edgecolors="black",
        marker="*",
        s=200,
        label="Destination"
    )

    # STEP 7: Mark current rover position.
    if rover_position is not None:

        ax.scatter(
            rover_position[1],
            rover_position[0],
            color="cyan",
            marker="s",
            s=100,
            label="Rover"
        )

    # STEP 8: Add labels and display.
    ax.set_title("MarsPath - Rover Navigation")
    ax.set_xlabel("Grid Column")
    ax.set_ylabel("Grid Row")

    ax.set_xticks(np.arange(-0.5, terrain.shape[1], 1))
    ax.set_yticks(np.arange(-0.5, terrain.shape[0], 1))

    ax.grid(color="gray", linewidth=0.5)
    ax.legend(loc="upper right")

    plt.tight_layout()
    plt.show()