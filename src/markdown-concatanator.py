from dotenv import load_dotenv
import os
from pathlib import Path

# Load environment variables from the .env file
load_dotenv()

# Grab the required environment variables
CV_MD_FOLDER = os.getenv('CV_MD_FOLDER')
COMBINED_CV_FILE = os.getenv('COMBINED_CV_FILE')

def concatenate_markdown_files(input_folder, output_file):
    """
    Concatenate all Markdown files in input_folder into a single output_file.
    
    Args:
        input_folder (str): Path to folder containing Markdown files
        output_file (str): Path to the output Markdown file
    """
    # Validate that folders are specified
    if not input_folder or not output_file:
        raise ValueError("CV_MD_FOLDER environment variable must be set")
    
    # Create Path objects
    input_path = Path(input_folder)
    output_path = Path(CV_MD_FOLDER + "/" + output_file)
    
    # Validate that input folder exists
    if not input_path.exists():
        raise FileNotFoundError(f"Input folder not found: {input_folder}")
    
    # Find all Markdown files in the input folder, excluding the output file if it lives there
    md_files = [md for md in input_path.glob("*.md") if md.name != output_file]
    
    if not md_files:
        print(f"No Markdown files found in {input_folder}")
        return
    
    # Concatenate contents of all Markdown files
    with output_path.open('w', encoding='utf-8') as outfile:
        for md_file in md_files:
            with md_file.open('r', encoding='utf-8') as infile:
                outfile.write("Filename: `" + md_file.name + "`\n\n") # Add filename as a header
                outfile.write(infile.read() + "\n\n")  # Add spacing between files
                outfile.write("---\n\n")  # Add a horizontal rule between files
            print(f"✓ Added {md_file.name} to {output_file}")


if __name__ == "__main__":
    try:
        concatenate_markdown_files(CV_MD_FOLDER, COMBINED_CV_FILE)
    except Exception as e:
        print(f"Error: {e}")