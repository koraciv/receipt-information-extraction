import pytesseract
from PIL import Image
import cv2

def extract_raw_text(processed_image):
    print("Executing Optical Character Recognition (OCR)...")
    
    # pytesseract requires a PIL Image, so we convert the OpenCV NumPy array
    pil_img = Image.fromarray(processed_image)
    
    # PSM 6 assumes a single uniform block of text (good for receipts)
    custom_config = r'--oem 3 --psm 6'
    
    raw_text = pytesseract.image_to_string(pil_img, config=custom_config)
    
    if not raw_text.strip():
        print("Warning: OCR extracted no text. Check image quality.")
        
    return raw_text
