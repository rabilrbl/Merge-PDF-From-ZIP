import sys
import os
import zipfile
from tempfile import TemporaryDirectory
from PyPDF2 import PdfReader, PdfWriter

# Get the zip file name from the command-line argument
zip_file_name = sys.argv[1]

# Create a temporary directory
with TemporaryDirectory() as temp_dir:
    # Open the zip file
    with zipfile.ZipFile(zip_file_name, 'r') as zip_ref:
        # Extract all PDF files to the temporary directory
        pdf_files = [file for file in zip_ref.namelist() if file.endswith('.pdf')]
        zip_ref.extractall(temp_dir)

    # Create a new PDF file writer
    output_pdf = PdfWriter()

    # Iterate through the list of PDF files
    for pdf in pdf_files:
        pdf = os.path.join(temp_dir, pdf)
        # Open each PDF file
        with open(pdf, 'rb') as pdf_file:
            # Create a new PDF file reader
            input_pdf = PdfReader(pdf_file)

            # Iterate through the pages of the input PDF
            for page_num in range(len(input_pdf.pages)):
                # Add the page to the output PDF
                output_pdf.add_page(input_pdf.pages[page_num])

    # Write the merged PDF to a file
    with open(zip_file_name.replace('.zip','') + '_merged.pdf', 'wb') as output:
        output_pdf.write(output)

# The temporary directory and its contents will be deleted automatically