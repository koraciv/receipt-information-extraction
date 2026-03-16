import re

def parse_receipt_data(raw_text):
    print("Parsing unstructured text into structured financial data...")
    lines = raw_text.split('\n')
    
    extracted_data = {
        "merchant_name": "Unknown",
        "date": "Unknown",
        "total_amount": None
    }
    
    # 1. Extract Merchant Name (Usually the very first non-empty line)
    for line in lines:
        if line.strip():
            extracted_data["merchant_name"] = line.strip()
            break
            
    # 2. Extract Date (Looking for DD.MM.YYYY or DD/MM/YYYY)
    date_pattern = r'\b(\d{1,2}[./-]\d{1,2}[./-]\d{2,4})\b'
    date_match = re.search(date_pattern, raw_text)
    if date_match:
        extracted_data["date"] = date_match.group(1)
        
    # 3. Extract Total Amount (Looking for "Total", "Summe", or "Betrag" followed by numbers)
    # Handles both EUR/USD formats: 12.34 or 12,34
    total_pattern = r'(?i)(?:total|summe|betrag)\s*[:]?\s*[\$€]?\s*(\d+[.,]\d{2})'
    total_match = re.search(total_pattern, raw_text)
    
    if total_match:
        # Normalize comma to dot for float conversion
        amount_str = total_match.group(1).replace(',', '.')
        extracted_data["total_amount"] = float(amount_str)
        
    return extracted_data
