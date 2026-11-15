import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob
import os



def process_image(folder_path):

    # Load image and check for failure.

    results = []

    # folder_path = r"/Users/taoyilei/Desktop/planeterrainer/images"
    image_paths = glob.glob(os.path.join(folder_path, "*.jpg")) + \
              glob.glob(os.path.join(folder_path, "*.png"))

    for image_path in image_paths:
           image = cv2.imread(image_path)
           if image is None:
                print(f"Failed to load: {image_path}")
                continue

           # Resize image to 200 x 200.
           resized = cv2.resize(image,(200,200))
           
            # Convert BGR image to texture evaluatio .
           gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY) #turn the image into grayscale for texture evaluation
           texture = cv2.Laplacian(gray, cv2.CV_64F) #evaluate the variation of brightness of the image using Laplacian operator

           texture = np.abs(texture) #sensing change in texture
           threshold = 15
          
           rock_detection = (texture > threshold).astype(np.uint8) * 255
           
           
            # Create an obstacle mask using HSV thresholds.
         
           
            # Clean the mask and expand obstacles.
           kernel = np.ones((5,5),np.uint8)
           mask_cleaned = cv2.morphologyEx(rock_detection, cv2.MORPH_OPEN, kernel)
           mask_dilated = cv2.dilate(mask_cleaned, kernel, iterations = 1)

           #cv2.imshow("Original Image", resized)
           cv2.imshow("Rock Detection", mask_dilated)

           cv2.waitKey(0)
           cv2.destroyAllWindows()

           results.append((mask_dilated))
           
           
           
            
    return results
           
           
                
  
   

    

    

if __name__ == "__main__":
    results = process_image()
    print("Total images processed:", len(results))