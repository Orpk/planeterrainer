import matplotlib.pyplot as plt
import numpy as np

import tkinter as tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import cv2
from PIL import Image, ImageTk

def display_results(img_path, grid =[[]], path =[[],[]], start = [0,0], goal = [0,0]):
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
    root = tk.Tk()
    root.wm_title("Traversal path")

    # img
    cv_img = 0
    if isinstance(img_path, str):
        cv_img = cv2.imread(img_path)
        cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
    # 2. Convert BGR to RGB
    else:
        cv_img = cv2.cvtColor(img_path, cv2.COLOR_BGR2RGB)

    height, width, channels = cv_img.shape


    root.geometry(f"{width+50}x{height+100}")
    # pil_img = Image.fromarray(cv_img)
    # img = pil_img.convert("RGBA")
    # r, g, b, a = img.split()
    # a = a.point(lambda p: int(p * 0.1))
    # img.putalpha(a)

    # Convert to Tkinter image
    # imgtk = ImageTk.PhotoImage(img, master=root)

    # imgtk = ImageTk.PhotoImage(pil_img)
    # label = tk.Label(root, image=imgtk, borderwidth=0)
    # label.image = imgtk  # Keep a reference to avoid garbage collection
    # width = imgtk.width()
    # height = imgtk.height()

    

    # grid plot
    plt.style.use('_mpl-gallery-nogrid')
    Z = grid
    fig, ax = plt.subplots(figsize=(width/100,height/100), dpi=100)
    scale = 10
    ax.plot([x * scale + scale/2 for x in path[0]],
    [y * scale + scale/2 for y in path[1]]) # path
    ax.plot(start[0]*scale + scale/2, start[1]*scale + scale/2, 'ro', markersize=10)
    ax.plot(goal[0]*scale + scale/2, goal[1]*scale + scale/2, 'go', markersize=10)
    plt.title("Traversal Path")    
    ax.imshow(Z, origin='upper', extent=(0, width, height, 0))

    ax.imshow(cv_img, extent=[0, width, height, 0], alpha=0)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()

    # alpha
    def update_alpha(new_val):
        # retrieve frequency
        f = 0
        f = float(new_val)

        # update data
        ax.imshow(cv_img, extent=[0, width, height, 0], alpha=f*0.2)

        # required to update canvas and attached toolbar!
        canvas.draw()

    slider_update = tk.Scale(root, from_=1, to=5, orient=tk.HORIZONTAL,
                              command=update_alpha, label="alpha")

    # toolbar
    toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
    toolbar.update()

    canvas.mpl_connect(
        "key_press_event", lambda event: print(f"you pressed {event.key}"))
    canvas.mpl_connect("key_press_event", key_press_handler)

    # quit btn
    button_quit = tk.Button(master=root, text="Quit", command=root.destroy)

    # place/pack
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    # label.place(x=0,y=0)
    # label.lift()
    button_quit.pack(side=tk.BOTTOM)
    toolbar.pack(side=tk.BOTTOM, fill=tk.X)
    slider_update.pack(side=tk.BOTTOM)

    # loop
    def on_close():
        root.destroy()
        root.quit()
    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()


if __name__ == "__main__":
    terrain_grid = [
    [0, 0, 0, 2, 0],
    [0, 1, 0, 3, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 4, 0],
    [6, 5, 0, 0, 0]]
    path = [[0,1,2,2,2,3,4,4,4],
            [0,0,0,1,2,2,2,3,4]]
    img_path = "images\\e3a-PIA26306-HiRISE-16x9.jpg"
    display_results(img_path, terrain_grid, path, [0,0], [4,4])