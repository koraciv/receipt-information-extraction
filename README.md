# Automated Receipt & Invoice Extraction (Computer Vision + NLP)

## 📌 Project Overview
Enterprise finance departments and retail master data teams process thousands of paper receipts, competitor pricing flyers, and vendor invoices daily. Manual data entry is slow, expensive, and highly prone to human error.

This project implements an automated **Information Extraction Pipeline**. It utilizes **OpenCV** to clean and preprocess raw, noisy images of receipts, applies **Tesseract OCR** to extract the optical text, and uses **Regex/NLP parsing** to identify and extract structured financial entities (Merchant Name, Transaction Date, and Total Amount).

**Business Value:** Digitizes unstructured physical documents into structured, queryable data, drastically reducing manual administrative overhead and accelerating financial reporting.

## 🛠️ Tech Stack
* **Computer Vision:** OpenCV (`cv2`) for image binarization and adaptive thresholding
* **Optical Character Recognition:** PyTesseract (Google Tesseract OCR engine)
* **Natural Language Processing:** Python `re` (Regex) for entity extraction
* **Language:** Python 3.x

## 🏗️ Architecture & Workflow
1. **CV Preprocessing (`image_processing.py`):** Loads receipt images and applies grayscale conversion and Gaussian adaptive thresholding to eliminate shadows and isolate text.
2. **Text Extraction (`ocr_engine.py`):** Passes the perfectly binarized image arrays to the Tesseract OCR engine to extract raw, multi-line strings.
3. **Entity Parsing (`information_extractor.py`):** Scans the unstructured OCR output using pattern matching to locate critical financial metadata, handling variations in currency formatting and languages.
4. **JSON Serialization (`main.py`):** Outputs the extracted variables into a clean JSON structure ready for database insertion or API delivery.

## 📂 Project Structure
```text
├── data/                   # Directory for sample receipt images (.jpg, .png)
├── src/                    
│   ├── image_processing.py # OpenCV image cleaning
│   ├── ocr_engine.py       # Tesseract text extraction
│   ├── information_extractor.py # Regex entity parsing
│   └── main.py             # Pipeline orchestrator
├── requirements.txt        # Python dependencies
├── .gitignore              # Ignored files and directories
└── README.md               # Project documentation
