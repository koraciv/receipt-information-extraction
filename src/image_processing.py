import cv2
import numpy as np

def preprocess_image(image_path):
    print(f"Loading and preprocessing image: {image_path}")
    
    # Read the image using OpenCV
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Could not load image at {image_path}")
        
    # 1. Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 2. Apply adaptive thresholding to isolate text from background
    # This handles uneven lighting (e.g., shadows on a crumpled receipt)
    processed_img = cv2.adaptiveThreshold(
        gray, 255, 
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY, 11, 2
    )
    
    # 3. Optional: Dilation/Erosion to thicken thin fonts could go here
    
    print("Image preprocessing complete.")
    return processed_img
