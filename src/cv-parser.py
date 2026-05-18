from dotenv import load_dotenv
import os
from pathlib import Path
import requests

# Load environment variables from the .env file
load_dotenv()

# Grab the required environment variables
CV_PDF_FOLDER = os.getenv('CV_PDF_FOLDER')
CV_MD_FOLDER = os.getenv('CV_MD_FOLDER')
NANONETS_API_KEY = os.getenv('NANONETS_API_KEY')
NANONETS_API_URL = os.getenv('NANONETS_API_URL')

def parse_pdf_to_markdown(input_folder, output_folder):
    """
    Parse all PDF files in input_folder to Markdown and write to output_folder.
    
    Args:
        input_folder (str): Path to folder containing PDF files
        output_folder (str): Path to folder where Markdown files will be written
    """
    # Validate that folders are specified
    if not input_folder or not output_folder:
        raise ValueError("CV_PDF_FOLDER and CV_MD_FOLDER environment variables must be set")
    
    # Create Path objects
    input_path = Path(input_folder)
    output_path = Path(output_folder)
    
    # Validate that input folder exists
    if not input_path.exists():
        raise FileNotFoundError(f"Input folder not found: {input_folder}")
    
    # Create output folder if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Find all PDF files in the input folder
    pdf_files = list(input_path.glob("*.pdf"))
    
    if not pdf_files:
        print(f"No PDF files found in {input_folder}")
        return
    
    headers = {
        'Authorization': f'Bearer {NANONETS_API_KEY}'
    }
    
    # Process each PDF file
    for pdf_file in pdf_files:
        try:
            print(f"Processing: {pdf_file.name}")
            
            # Create output markdown filename (replace .pdf with .md)
            output_file = output_path / (pdf_file.stem.replace(" ", "_") + ".md")

            # Check if output file already exists            
            if output_file.exists():
                print(f"✓ Skipping {pdf_file.name} (already converted)")
                continue

            response = requests.post(NANONETS_API_URL, 
                files={ 'file': open(pdf_file, 'rb') },
                data={'output_type': 'markdown'},
                headers=headers
            )

            print(f"Writing to: {output_file.name}")
            
            # Write markdown content to output file
            response_json = response.json()
            output_file.write_text(response_json["content"], encoding="utf-8")
            print(f"✓ Converted to: {output_file.name}")
            
        except Exception as e:
            print(f"✗ Error processing {pdf_file.name}: {e}")
    
    print(f"\nConversion complete. Output files written to: {output_folder}")


if __name__ == "__main__":
    try:
        parse_pdf_to_markdown(CV_PDF_FOLDER, CV_MD_FOLDER)
    except Exception as e:
        print(f"Error: {e}")

