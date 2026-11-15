import cv2
import numpy as np

def process_image(image_path):
    """
    STEP 1: Load the image from the specified file path.
        - Use cv2.imread().
        - Check whether the image loaded successfully.
        - Raise an error if the file does not exist.

    STEP 2: Resize the image.
        - Use cv2.resize().
        - Aim for 200 x 200 pixels.
        - Smaller images make processing faster.

    STEP 3: Convert the image from BGR to HSV.
        - Use cv2.cvtColor().
        - HSV makes colour-based segmentation easier.

    STEP 4: Identify potential obstacles.
        - Use cv2.inRange() to create a binary mask.
        - White pixels (255) represent potential obstacles.
        - Black pixels (0) represent other terrain.
        - Tune the HSV thresholds to your chosen image.

    STEP 5: Clean up the mask.
        - Use cv2.morphologyEx() to remove small noise.
        - Use cv2.dilate() to expand obstacles for rover safety.

    STEP 6: Return both the resized image and obstacle mask.

    IMPORTANT:
        Colour thresholds are only reliable when the image has
        predictable colours. For ordinary NASA photographs,
        use manual obstacle corrections or a separate test map.

    GUIDE:
    https://docs.opencv.org/4.x/da/d97/tutorial_threshold_inRange.html
    https://docs.opencv.org/4.x/d9/d61/tutorial_py_morphological_ops.html
    """

    

    # TODO 1: Load image and check for failure.

    # TODO 2: Resize image to 200 x 200.

    # TODO 3: Convert BGR image to HSV.

    # TODO 4: Create an obstacle mask using HSV thresholds.

    # TODO 5: Clean the mask and expand obstacles.

    # TODO 6: Return image and mask.

    pass