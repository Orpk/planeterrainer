import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob
import os

"""
   STEP 1: Load the image from the specified file path.
        - Use cv2.imread().
        - Check whether the image loaded successfully.
        - Raise an error if the file does not exist.
    
    image = cv2.imread()

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


def process_image():

    # TODO 1: Load image and check for failure.

    results = []

    folder_path = r"/Users/taoyilei/Desktop/planeterrainer/images"
    image_paths = glob.glob(os.path.join(folder_path, "*.jpg")) + \
              glob.glob(os.path.join(folder_path, "*.png"))

    for image_path in image_paths:
           image = cv2.imread(image_path)
           if image is None:
                print(f"Failed to load: {image_path}")
                continue

           # TODO 2: Resize image to 200 x 200.
           resized = cv2.resize(image,(200,200))
           
            # TODO 3: Convert BGR image to texture evaluatio .
           gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY) #turn the image into grayscale for texture evaluation
           texture = cv2.Laplacian(gray, cv2.CV_64F) #evaluate the variation of brightness of the image using Laplacian operator

           texture = np.abs(texture) #sensing change in texture
           threshold = 15
          
           rock_detection = (texture > threshold).astype(np.uint8) * 255
           
           
            # TODO 4: Create an obstacle mask using HSV thresholds.
          # lower_bound = np.array([5, 90, 80])
           #upper_bound = np.array([22, 255, 240]) #mars dusts has a hue of 5-22, saturation of 90-255, and value of 80-240
            #hue of 5-22 matches with the orange-raddish color on Mars surface
            #saturation of 90-255 matches with the dusty and dry surface of Mars
            #value of 80-240 matches with the brightness of the surface
           #mask = cv2.inRange(hsv, lower_bound, upper_bound)
          # rock_detection = cv2.bitwise_not(mask)
           
            # TODO 5: Clean the mask and expand obstacles.
           kernel = np.ones((5,5),np.uint8)
           mask_cleaned = cv2.morphologyEx(rock_detection, cv2.MORPH_OPEN, kernel)
           mask_dilated = cv2.dilate(mask_cleaned, kernel, iterations = 1)

           cv2.imshow("Original Image", resized)
           cv2.imshow("Rock Detection", mask_dilated)

           cv2.waitKey(0)
           cv2.destroyAllWindows()

           results.append((resized, mask_dilated))
           
           
           
            # TODO 6: Return image and mask.
    return results
           
           
                
  
   

    

    


results = process_image()
print("Total images processed:", len(results))