import matplotlib.pyplot as plt
import numpy as np


def display_results(grid =[[]], path =[[],[]], start = [0,0], goal = [0,0]):
    """
    1. Convert the grid into an image-friendly array.
    2. Display the grid using Matplotlib.
    3. Mark obstacles in black.
    4. Mark traversable cells in a contrasting colour.
    5. Draw the calculated path.
    6. Highlight the starting point and destination.
    7. Add a title and legend.

    Guides:
    - https://matplotlib.org/stable/plot_types/arrays/imshow.html
    - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
    """
    y = len(grid)
    x = len(grid[0])

    plt.style.use('_mpl-gallery-nogrid')

    # make data
    X, Y = np.meshgrid(np.linspace(0, x, 16), np.linspace(0, y, 16))
    # Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2 - Y**2)
    Z = grid
    # plot
    fig, ax = plt.subplots()
    plt.plot(path[0], path[1]) # path
    plt.plot(start[0], start[1], 'ro', markersize=10)
    plt.plot(goal[0], goal[1], 'go', markersize=10)
    plt.title("Traversal Path")    

    ax.imshow(Z, origin='lower')

    plt.show()


if __name__ == "__main__":
    terrain_grid = [
    [0, 0, 0, 2, 0],
    [0, 1, 0, 3, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 4, 0],
    [6, 5, 0, 0, 0]]
    path = [[0,1,2,2,2,3,4,4,4],
            [0,0,0,1,2,2,2,3,4]]
    display_results(terrain_grid, path, [0,0], [4,4])