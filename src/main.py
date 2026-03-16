import os
import json
from image_processing import preprocess_image
from ocr_engine import extract_raw_text
from information_extractor import parse_receipt_data

def run_extraction_pipeline():
    # Provide path to a sample receipt image for the portfolio
    image_path = "../data/sample_receipt.jpg"
    
    if not os.path.exists(image_path):
        print(f"Error: Please place a sample receipt image at {image_path}")
        print("Note: To run this locally, you must install the Tesseract-OCR binary on your OS.")
        return

    try:
        # Step 1: Computer Vision Preprocessing
        clean_image = preprocess_image(image_path)
        
        # Step 2: OCR Text Extraction
        raw_text = extract_raw_text(clean_image)
        
        # Step 3: NLP Parsing
        structured_data = parse_receipt_data(raw_text)
        
        print("\n================ EXTRACTION RESULTS ================")
        print(json.dumps(structured_data, indent=4))
        print("====================================================")

    except Exception as e:
        print(f"Pipeline failed: {e}")

if __name__ == "__main__":
    run_extraction_pipeline()
