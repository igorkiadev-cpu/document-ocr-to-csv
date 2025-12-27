"""
Document OCR to CSV
Prototype script for extracting structured data from delivery notes.
"""

import csv

def extract_data_from_document(file_path):
    """
    Simulated OCR extraction.
    In a real scenario, OCR logic would be applied here.
    """
    return {
        "supplier": "Sample Supplier",
        "delivery_note_ref": "DN-001",
        "date": "2024-01-01",
        "product_code": "PRD-001",
        "quantity": 10
    }

def export_to_csv(data, output_file="output.csv"):
    with open(output_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data.keys())
        writer.writerow(data.values())

if __name__ == "__main__":
    document_path = "sample_delivery_note.pdf"
    extracted_data = extract_data_from_document(document_path)
    export_to_csv(extracted_data)
    print("CSV file generated successfully.")
